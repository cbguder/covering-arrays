#!/usr/bin/env python

import sys
import os.path

from models import *
from generators import *

def main():
	if len(sys.argv) < 4:
		print 'USAGE: table-to-arff.py CONFIGURATION_MODEL TABLE TARGET_DIR'
		sys.exit(2)

	configuration_model = ConfigurationModel.from_xml(sys.argv[1])
	table = Table.from_file(sys.argv[2])
	generator = ARFFGenerator(configuration_model.options, table.test_runs)

	for test in table.tests:
		t = Test()
		t.name = test

		for error in table.errors[test]:
			output = test + '_' + error
			path = os.path.join(sys.argv[3], os.path.basename(sys.argv[2])[:-6] + '.' + output + '.arff')

			f = open(path, 'w')
			f.write(generator.generate(t, error))
			f.write('\n')
			f.close()

if __name__ == '__main__':
	main()
