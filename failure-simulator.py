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
	                  help='output file (defaults to STDOUT)')
	parser.add_option('-f', '--format',
	                  choices=['xml', 'arff', 'table'],
	                  help='output format: xml, arff or table [default: table]')
	parser.add_option('--no-errors',
	                  action='store_false',
	                  dest='errors')
	parser.set_defaults(format='table', errors=True)
	(options, args) = parser.parse_args()

	config_model   = ConfigurationModel.from_xml(args[0])
	covering_array = parse_csv(args[1])
	failure_model  = FailureModel.from_xml(args[2])

	test_runs = generate_test_runs(config_model, covering_array, failure_model.tests)

	if options.format == 'table':
		table  = generate_table(test_runs, config_model.options, failure_model.tests)
		output = array_to_ascii_table(table)
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
		output = generate_xml(test_runs).toxml()

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
				f = open(options.output + '.' + k, 'w')
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

def generate_table(test_runs, options, tests):
	table = []

	h_options = [option.name for option in options]
	h_tests   = [test.name for test in tests]

	header = h_options + h_tests
	table.append(header)

	for test_run in test_runs:
		row = []
		for option in h_options:
			row.append(test_run['configuration'][option])
		for test in h_tests:
			row.append(test_run['results'][test])
		table.append(row)
	
	return table

def array_to_ascii_table(table):
	output = []
	num_columns   = len(table[0])
	column_widths = [max([len(row[i]) for row in table]) for i in range(num_columns)]

	separator = '+-' + '-+-'.join(['-'*column_widths[i] for i in range(num_columns)]) + '-+'

	for row in table:
		line =  '| ' + ' | '.join([row[i].ljust(column_widths[i]) for i in range(num_columns)]) + ' |'
		output.append(line)
	
	output.insert(0, separator)
	output.insert(2, separator)
	output.append(separator)

	return '\n'.join(output)

def generate_xml(test_runs):
	doc  = Document()

	root = doc.createElement('runs')
	doc.appendChild(root)

	for test_run in test_runs:
		run           = doc.createElement('run')
		configuration = doc.createElement('configuration')
		results       = doc.createElement('results')

		for k, v in test_run['configuration'].iteritems():
			if k != '':
				option = doc.createElement('option')
				option.setAttribute('name', k)
				value  = doc.createTextNode(v)
				option.appendChild(value)
				configuration.appendChild(option)

		for k, v in test_run['results'].iteritems():
			test = doc.createElement('test')
			test.setAttribute('name', k)
			result = doc.createTextNode(v)
			test.appendChild(result)
			results.appendChild(test)

		run.appendChild(configuration)
		run.appendChild(results)
		root.appendChild(run)

	return doc

def parse_csv(file):
	f      = open(file, 'rb')
	reader = DictReader(f)
	rows   = [row for row in reader]
	f.close()

	return rows

if __name__ == '__main__':
	main()
