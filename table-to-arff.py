#!/usr/bin/env python

import sys
import os.path

from models import *
from generators import *

def main():
	if len(sys.argv) < 3:
		print 'USAGE: table-to-arff.py CONFIGURATION_MODEL TABLE'
		sys.exit(2)

	configuration_model = ConfigurationModel.from_xml(sys.argv[1])

	f = open(sys.argv[2])
	lines = f.readlines()
	f.close()

	header    = get_parts(lines[1])
	options   = []
	tests     = []
	errors    = {}
	test_runs = []

	for p in header:
		if p.startswith('o'):
			options.append(p)
		elif p.startswith('t'):
			tests.append(p)
	
	for test in tests:
		errors[test] = []

	l_options = len(options)
	l_tests   = len(tests)

	for line in lines[3:-1]:
		test_run = { 'configuration': {}, 'results': {} }
		parts = get_parts(line)

		for i in range(l_options):
			test_run['configuration'][options[i]] = parts[i]

		for i in range(l_tests):
			result = parts[l_options+i]
			test_run['results'][tests[i]] = result
			if result != 'p' and result not in errors[tests[i]]:
				errors[tests[i]].append(result)

		test_runs.append(test_run)
	
	generator = ARFFGenerator(configuration_model.options, test_runs)

	for test in tests:
		t = Test()
		t.name = test

		for error in errors[test]:
			output = test + '_' + error
			path = os.path.dirname(os.path.abspath(sys.argv[2]))
			path = os.path.join(path, '..', 'arff')
			path = os.path.normpath(path)
			path = os.path.join(path, os.path.basename(sys.argv[2])[:-6] + '.' + output + '.arff')

			f = open(path, 'w')
			f.write(generator.generate(t, error))
			f.write('\n')
			f.close()

def get_parts(str):
	parts = str.split('|')
	parts = [p.strip() for p in parts if p != '']
	return parts

if __name__ == '__main__':
	main()
