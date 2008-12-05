#!/usr/bin/env python

from xml.dom.minidom import Document as _Document

class XMLGenerator:
	def __init__(self):
		self.__init__(None)

	def __init__(self, test_runs):
		self.test_runs = test_runs

	def generate(self):
		doc  = _Document()

		root = doc.createElement('runs')
		doc.appendChild(root)

		for test_run in self.test_runs:
			run           = doc.createElement('run')
			configuration = doc.createElement('configuration')
			results       = doc.createElement('results')

			for k, v in test_run['configuration'].iteritems():
				if k != '':
					option = doc.createElement('option')
					option.setAttribute('name', k)
					value  = doc.createTextNode(v)
					option.appendChild(value)
					configuration.appendChild(option)

			for k, v in test_run['results'].iteritems():
				test = doc.createElement('test')
				test.setAttribute('name', k)
				result = doc.createTextNode(v)
				test.appendChild(result)
				results.appendChild(test)

			run.appendChild(configuration)
			run.appendChild(results)
			root.appendChild(run)

		return doc.toxml()
