#!/usr/bin/env python

import os
import sys
from subprocess import Popen

tables_path = 'test/final/simulation_results/table'

for file in os.listdir(tables_path):
	part = '-'.join(file.split('-')[:2])
	configuration_model = 'test/final/configuration_models/%s.xml' % part
	if os.path.exists(configuration_model):
		p = Popen(['./table-to-arff.py',
		           configuration_model,
		           tables_path + '/' + file])
		p.wait()
