#!/usr/bin/env python

import sys
import os.path

from models import *
from generators import *

def main():
	if len(sys.argv) < 3:
		print 'USAGE: table-to-xml.py FAILURE_MODEL TABLE'
		sys.exit(2)

	failure_model = FailureModel.from_xml(sys.argv[1])
	table = Table.from_file(sys.argv[2])
	generator = XMLGenerator(failure_model.tests, table.test_runs)
	print generator.generate()

if __name__ == '__main__':
	main()
