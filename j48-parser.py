#!/usr/bin/env python

import re
import sys
from optparse import OptionParser

from models import DecisionForest, DecisionTree

def main():
	parser = OptionParser(usage='Usage: %prog [OPTIONS] J48-TREE [J48-TREE...]',
	                      version='%prog 0.2')
	parser.add_option('-t', '--tidy',
	                  action='store_true',
	                  help='use uTidyLib to generate pretty output')
	parser.set_defaults(tidy=False)
	(options, args) = parser.parse_args()

	if len(args) < 1:
		parser.print_help()
		sys.exit(2)

	if options.tidy:
		import tidy

	forest = DecisionForest()

	for file in args:
		test = error = ''
		m = re.search('(t[0-9]+)_(e[0-9]+)', file)
		if m:
			test = m.group(1)
			error = m.group(2)

		f = open(file)
		tree = DecisionTree.from_file(f)
		tree.test  = test
		tree.error = error
		forest.trees.append(tree)
		f.close()

	output = forest.to_xml()

	if options.tidy:
		print str(tidy.parseString(output, input_xml=True, indent=True)),
	else:
		print output

if __name__ == '__main__':
	main()
