#!/usr/bin/env python

import sys
import random
from optparse import OptionParser

from models import *

def main():
	parser = OptionParser(usage='Usage: %prog [options] CONFIGURATION_MODEL',
	                      version='%prog 0.2')
	parser.add_option('-t', '--tests',
	                  type='int',
	                  metavar='NUM',
	                  help='number of tests [default: 2]')
	parser.add_option('-e', '--errors',
	                  type='int',
	                  metavar='NUM',
	                  help='number of errors [default: 2]')
	parser.add_option('-f', '--failures',
	                  help='number and size of failures (e.g. 2x2,3x5) [default: 2x2]')
	parser.set_defaults(errors=2, tests=2)
	(options, args) = parser.parse_args()

	if(len(args) < 1):
		parser.print_help()
		sys.exit()
	
	failures = parse_failures(options.failures)
	configuration_model = ConfigurationModel.from_xml(args[0])
	
	failure_model = generate_failures(configuration_model.options, options.tests, options.errors, failures)
	
	print failure_model.to_xml()

def parse_failures(failures):
	result = []
	if failures == None:
		return [(2,2)]
	parts = failures.split(',')
	for p in parts:
		sub_parts = map(int, p.strip().split('x'))
		if len(sub_parts) == 2:
			result.append(tuple(sub_parts))
	return result

def generate_failures(options, tests, errors, failures):
	failure_model = FailureModel()
	for i in range(tests):
		test = Test()
		test.name = 't%d' % (i+1)
		available_errors = range(1, errors+1)
		for count,size in failures:
			for j in range(count):
				try:
					picked_options = random.sample(options, size)
				except:
					print "ERROR: Number of requested options exceeds the number of available options."
					sys.exit()

				picked_values  = [random.choice(option.values) for option in picked_options]
				pattern = FailurePattern()

				try:
					error = random.choice(available_errors)
				except:
					print "ERROR: Number of requested failures exceeds the number of errors."
					sys.exit()

				available_errors.remove(error)
				pattern.result = 'e%d' % error
				for k in range(size):
					pattern.options[picked_options[k].name] = picked_values[k]
				test.patterns.append(pattern)
		failure_model.tests.append(test)
	return failure_model

if __name__ == '__main__':
	main()
