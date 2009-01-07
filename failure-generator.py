#!/usr/bin/env python

import sys
import random
from optparse import OptionParser, OptionValueError

from models import *

def main():
	parser = OptionParser(usage='Usage: %prog [options] CONFIGURATION_MODEL',
						  version='%prog 0.2')
	parser.add_option('-e', '--errors',
					  type='int',
					  metavar='NUM',
					  help='number of errors [default: 2]')
	parser.add_option('-f', '--failures',
					  type='string',
					  action='callback',
					  callback=parse_failures,
					  help='number and size of failures (e.g. 2x2,3x5) [default: 2x2]')
	parser.add_option('--min-failures',
					  type='int',
					  metavar='NUM',
					  action='callback',
					  callback=failures_callback,
					  help='minimum failures per test [default: 1]')
	parser.add_option('--max-failures',
					  type='int',
					  metavar='NUM',
					  action='callback',
					  callback=failures_callback,
					  help='maximum failures per test [default: 2]')
	parser.add_option('--min-coverage',
					  type='int',
					  metavar='NUM',
					  action='callback',
					  callback=coverage_callback,
					  help='minimum option coverage [default: 10%]')
	parser.add_option('--max-coverage',
					  type='int',
					  metavar='NUM',
					  action='callback',
					  callback=coverage_callback,
					  help='maximum option coverage [default: 80%]')
	parser.add_option('-t', '--tidy',
	                  action='store_true',
	                  help='use uTidyLib to generate pretty output')
	parser.set_defaults(errors=2,
						failures=[(2,2)],
						min_failures=1,
						max_failures=2,
						min_coverage=10,
						max_coverage=80,
	                    tidy=False)
	(options, args) = parser.parse_args()

	if len(args) < 1:
		parser.print_help()
		sys.exit(2)

	if options.tidy:
		import tidy

	configuration_model = ConfigurationModel.from_xml(args[0])

	failure_model = generate_failures(configuration_model.options, options)
	output = failure_model.to_xml()

	if options.tidy:
		print str(tidy.parseString(output, input_xml=True, indent=True)),
	else:
		print output

def parse_failures(option, opt, value, parser):
	result = []
	parts = value.split(',')
	for p in parts:
		try:
			sub_parts = map(int, p.strip().split('x'))
		except:
			raise OptionValueError('option %s: invalid value: %s' % (opt, value))

		if len(sub_parts) == 2:
			result.append(tuple(sub_parts))
		else:
			raise OptionValueError('option %s: invalid value: %s' % (opt, value))
	setattr(parser.values, option.dest, result)

def failures_callback(option, opt_str, value, parser):
	if value < 1:
		raise OptionValueError('option %s: value < 1' % opt_str)

	if (option.dest == 'min_failures' and value > parser.values.max_failures) or \
	   (option.dest == 'max_failures' and value < parser.values.min_failures):
			raise OptionValueError('option min-failures > max-failures')

	setattr(parser.values, option.dest, value)

def coverage_callback(option, opt_str, value, parser):
	if value < 0:
		raise OptionValueError('option %s: value < 0' % opt_str)

	if value > 100:
		raise OptionValueError('option %s: value > 100' % opt_str)

	if (option.dest == 'min_coverage' and value > parser.values.max_coverage) or \
	   (option.dest == 'max_coverage' and value < parser.values.min_coverage):
		raise OptionValueError('option min-coverage > max-coverage')

	setattr(parser.values, option.dest, value)

def generate_failures(options, args):
	tests = None
	failures = sum([[f[1]] * f[0] for f in args.failures], [])

	# Generate test-failure configuration
	P = greedy_partition(len(failures), range(args.min_failures, args.max_failures+1))

	# 6 is completely arbitrary
	for i in range(6):
		temp_tests = slice_list(failures, P)
		if args.min_coverage <= min_coverage(temp_tests, options) <= args.max_coverage:
			tests = temp_tests
			break
		random.shuffle(failures)

	if tests == None:
		print "ERROR: Cannot find test configuration."
		sys.exit(1)

	# Eliminate some options to make sure we don't exceed maximum option coverage
	c = len(options)
	to_eliminate = c - c * args.max_coverage / 100
	eliminated = random.sample(options, to_eliminate)
	for option in eliminated:
		options.remove(option)

	failure_model = FailureModel()
	for i, t in enumerate(tests):
		test = Test()
		test.name = 't%d' % (i+1)
		available_errors  = range(1, args.errors+1)
		available_options = options[:]
		for size in t:
			try:
				picked_options = random.sample(available_options, size)
				for option in picked_options:
					available_options.remove(option)
			except:
				print "ERROR: Number of requested options exceeds the number of available options."
				sys.exit(1)

			picked_values = [random.choice(option.values) for option in picked_options]
			pattern = FailurePattern()

			try:
				error = random.choice(available_errors)
			except:
				print "ERROR: Number of requested failures exceeds the number of errors."
				sys.exit(1)

			available_errors.remove(error)
			pattern.result = 'e%d' % error
			for k in range(size):
				pattern.options[picked_options[k].name] = picked_values[k]
			test.patterns.append(pattern)
		failure_model.tests.append(test)
	return failure_model

def greedy_partition(n, L):
	partition = []

	while n > 0:
		try:
			p = max([l for l in L if l <= n])
		except:
			return None

		n -= p
		partition.append(p)

	return partition

def min_coverage(tests, options):
	coverage = max([sum(test) for test in tests])
	return 100.0 * coverage / len(options)

def slice_list(L, P):
	result = []
	i = 0
	for p in P:
		result.append(L[i:i+p])
		i += p
	return result

if __name__ == '__main__':
	main()
