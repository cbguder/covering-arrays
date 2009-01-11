#!/usr/bin/env python

import sys
from models import *

def main():
	if len(sys.argv) < 3:
		print "Usage: configuration-generator.py NUM_OPTIONS NUM_VALUES"
		sys.exit(2)

	try:
		num_options = int(sys.argv[1])
		num_values  = int(sys.argv[2])
	except:
		print "Usage: configuration-generator.py NUM_OPTIONS NUM_VALUES"
		sys.exit(1)

	print generate_configuration(num_options, num_values)

def generate_configuration(num_options, num_values):
	model = ConfigurationModel()

	for i in range(num_options):
		option = Option('o%d' % (i+1))
		option.values = range(num_values)
		model.options.append(option)
	
	return model.to_xml()

if __name__ == '__main__':
	main()
