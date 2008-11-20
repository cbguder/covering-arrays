#!/usr/bin/env python

import sys
from csv import DictReader
from xml.dom.minidom import Document, parse
from FailureModel import Test, FailurePattern
from ConfigurationModel import ConfigurationModel

def main(argv):
	if len(argv) < 3:
		print "Usage: failure-simulator.py MODEL COVERING-ARRAY FAILURE-PATTERNS"
		sys.exit()
	
	config_model   = ConfigurationModel(argv[0])
	covering_array = parse_csv(argv[1])
	fail_patterns  = parse_failure_patterns(argv[2])

	test_runs = generate_test_runs(config_model, covering_array, fail_patterns)
	table     = generate_table(test_runs, config_model.options, fail_patterns)

	print array_to_ascii_table(table)

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

def parse_failure_patterns(file):
	tests = []
	dom   = parse(file)

	test_nodes = dom.getElementsByTagName('test')
	for test in test_nodes:
		tests.append(Test(test))
	
	return tests

if __name__ == '__main__':
	main(sys.argv[1:])
