#!/usr/bin/env python

import sys
import random
from optparse import OptionParser

from models import *

def main():
	parser = OptionParser(usage='Usage: %prog [options] CONFIGURATION_MODEL',
	                      version='%prog 0.1')
	parser.add_option('-t', '--tests',
	                  type='int',
	                  metavar='NUM',
	                  help='number of tests (defaults to 2)')
	parser.add_option('-e', '--errors',
	                  type='int',
	                  metavar='NUM',
	                  help='number of errors (defaults to 4)')
	parser.add_option('-o', '--output',
	                  metavar='FILE',
	                  help='output file (defaults to STDOUT)')
	parser.add_option('-f', '--failures',
	                  help='number and size of failures (e.g. 2x2,3x5, defaults to 2x2)')
	parser.set_defaults(errors=4, tests=2)
	(options, args) = parser.parse_args()
	
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
		for count,size in failures:
			for j in range(count):
				picked_options = random.sample(options, size)
				picked_values  = [random.choice(option.values) for option in picked_options]
				pattern = FailurePattern()
				pattern.result = 'e%d' % (random.randrange(errors) + 1)
				for k in range(size):
					pattern.options[picked_options[k].name] = picked_values[k]
				test.patterns.append(pattern)
		failure_model.tests.append(test)
	return failure_model

if __name__ == '__main__':
	main()
