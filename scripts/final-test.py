#!/usr/bin/env python

import os
import sys
from subprocess import Popen

for file in os.listdir('failure_patterns'):
	parts = file.split('-')
	part = '-'.join(parts[:2])
	failure_pattern     = 'failure_patterns/' + file
	configuration_model = 'configuration_models/%s.xml' % part
	if os.path.exists(configuration_model):
		for t in range(2, 6):
			covering_array = 'covering_arrays/%s-%d.csv' % (part, t)
			if os.path.exists(covering_array):
				if os.path.exists('simulation_results/decision-tree/%s-%d-%s' % (part, t, '-'.join(parts[2:]))):
					print 'SKIP ' + file
				else:
					p = Popen(['../../scripts/final-test',
					           configuration_model,
					           covering_array,
					           failure_pattern])
					p.wait()
