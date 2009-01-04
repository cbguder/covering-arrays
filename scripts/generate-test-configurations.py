#!/usr/bin/env python

import sys
import os.path
sys.path.append(os.path.normpath(os.path.join(sys.path[0], '..')))

from models import *

for num_options in range(5, 21, 5):
	for num_values in range(2, 6):
		model = ConfigurationModel()

		for i in range(num_options):
			option = Option('o%d' % (i+1))
			option.values = range(num_values)
			model.options.append(option)

		f = open('%d-%d.xml' % (num_options, num_values), 'w')
		f.write(model.to_xml())
		f.close()
