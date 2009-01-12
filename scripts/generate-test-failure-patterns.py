#!/usr/bin/env python

import os
import sys
import os.path
from subprocess import Popen

root = os.path.normpath(os.path.join(sys.path[0], '..'))
sys.path.append(root)
from models import *

for xml in sys.argv[1:]:
	for failure_configuration in range(1, 6):
		for coverage in [10, 20, 40, 60, 80, 100]:
			for max_failures in range(1, 6):
				f = open(os.path.join(root, 'test', 'final', 'failure_patterns', '%s-%d-%d-%d.xml' % (os.path.basename(xml)[:-4], failure_configuration, coverage, max_failures)), 'w')
				p = Popen([os.path.join(root, 'failure-generator.py'),
				           '--errors=20',
				           '--failures=50x%d' % failure_configuration,
				           '--max-coverage=%d' % coverage,
				           '--min-coverage=%d' % coverage,
				           '--max-failures=%d' % max_failures,
				           xml],
				          stdout=f)
				f.close()
