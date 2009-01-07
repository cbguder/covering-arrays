#!/usr/bin/env python

import re
import sys
from optparse import OptionParser

from models import DecisionTree, DecisionTreeNode

def main():
	parser = OptionParser(usage='Usage: %prog J48-TREE',
	                      version='%prog 0.2')
	parser.add_option('-t', '--tidy',
	                  action='store_true',
	                  help='use uTidyLib to generate pretty output')
	parser.set_defaults(tidy=False)
	(options, args) = parser.parse_args()

	if len(args) < 1:
		parser.print_help()
		sys.exit()

	if options.tidy:
		import tidy

	f = open(args[0])
	dtree = DecisionTree.from_file(f)
	f.close()

	output = dtree.to_xml()

	if options.tidy:
		print str(tidy.parseString(output, input_xml=True, indent=True)),
	else:
		print output

if __name__ == '__main__':
	main()
