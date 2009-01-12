#!/usr/bin/env python

import os
import sys
from subprocess import Popen

for file in os.listdir('test/final/failure_patterns'):
	part = '-'.join(file.split('-')[:2])
	failure_pattern = 'test/final/failure_patterns/' + file
	configuration_model = 'test/final/configuration_models/%s.xml' % part
	if os.path.exists(configuration_model):
		for t in range(2, 5):
			covering_array = 'test/final/covering_arrays/%s-%d.csv' % (part, t)
			if os.path.exists(covering_array):
				p = Popen(['./failure-simulator.py',
				           '--format=table',
				           '--output=test/final/simulation_results/%s-%d.table' % (file[:-4], t),
				           configuration_model,
				           covering_array,
				           failure_pattern])
				p.wait()
