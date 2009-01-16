#!/usr/bin/env python

import os
import sys
from subprocess import Popen

for file in os.listdir('failure_patterns'):
	if os.path.exists('simulation_results/decision-tree/' + file):
		print 'SKIP ' + file
	else:
		parts = file.split('-')
		failure_pattern     = 'failure_patterns/' + file
		configuration_model = 'configuration_models/%s.xml' % '-'.join(parts[:2])
		covering_array      = 'covering_arrays/%s.csv' % '-'.join(parts[:3])
		if os.path.exists(configuration_model) and os.path.exists(covering_array):
				p = Popen(['../../scripts/final-test',
				           configuration_model,
				           covering_array,
				           failure_pattern])
				p.wait()
