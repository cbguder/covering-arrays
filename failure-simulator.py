#!/usr/bin/env python

import sys
from csv import DictReader
from optparse import OptionParser
from xml.dom.minidom import Document

from models import *
from generators import *

def main():
	parser = OptionParser(usage='Usage: %prog [options] MODEL COVERING_ARRAY FAILURE_PATTERNS',
	                      version='%prog 0.2')
	parser.add_option('-o', '--output',
	                  metavar='FILE',
	                  help='output file (or basename for arff) [default: STDOUT]')
	parser.add_option('-f', '--format',
	                  choices=['xml', 'arff', 'table'],
	                  help='output format: xml, arff or table [default: table]')
	parser.add_option('--no-errors',
	                  action='store_false',
	                  dest='errors',
					  help='generate ARFF output for each test only')
	parser.add_option('-t', '--tidy',
	                  action='store_true',
	                  help='use uTidyLib to generate pretty output')
	parser.set_defaults(format='table',
	                    errors=True,
	                    tidy=False)
	(options, args) = parser.parse_args()

	if len(args) < 3:
		parser.print_help()
		sys.exit(2)

	if options.tidy:
		import tidy

	config_model   = ConfigurationModel.from_xml(args[0])
	covering_array = parse_csv(args[1])
	failure_model  = FailureModel.from_xml(args[2])

	test_runs = generate_test_runs(config_model, covering_array, failure_model.tests)

	if options.format == 'table':
		generator = TableGenerator(config_model.options, failure_model.tests, test_runs)
		output = generator.generate()
	elif options.format == 'arff':
		generator = ARFFGenerator(config_model.options, test_runs)
		output = {}
		for test in failure_model.tests:
			if options.errors:
				for pattern in test.patterns:
					output_name = '%s_%s' % (test.name, pattern.result)
					output[output_name] = generator.generate(test, pattern.result)
			else:
				output[test.name] = generator.generate(test)
	elif options.format == 'xml':
		generator = XMLGenerator(failure_model.tests, test_runs)
		output = generator.generate()
		if options.tidy:
			output = str(tidy.parseString(output, input_xml=True, indent=True)).strip()

	if options.output == None:
		if options.format == 'arff':
			for k, v in output.iteritems():
				print v
				print
		else:
			print output
	else:
		if options.format == 'arff':
			for k, v in output.iteritems():
				filename = '%s-%s.arff' % (options.output, k)
				f = open(filename, 'w')
				f.write(v)
				f.write('\n')
				f.close()
		else:
			f = open(options.output, 'w')
			f.write(output)
			f.write('\n')
			f.close()

def generate_test_runs(configuration_model, covering_array, failure_patterns):
	test_runs = []
	for test_configuration in covering_array:
		test_run = {'configuration': test_configuration, 'results': {}}
		for test in failure_patterns:
			result = test.run_with_configuration(test_configuration)
			test_run['results'][test.name] = result
		test_runs.append(test_run)

	return test_runs

def parse_csv(file):
	f      = open(file)
	reader = DictReader(f)
	rows   = [row for row in reader if 'DC.DC' not in row.values()]
	f.close()

	return rows

if __name__ == '__main__':
	main()
