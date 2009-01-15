#!/usr/bin/env python

from xml.dom.minidom import Document as _Document

class XMLGenerator:
	def __init__(self):
		self.__init__(None)

	def __init__(self, tests, test_runs):
		self.tests     = tests
		self.test_runs = test_runs

	def generate(self):
		doc  = _Document()

		root = doc.createElement('results')
		doc.appendChild(root)

		for test in self.tests:
			test_node = doc.createElement('test')
			test_node.setAttribute('name', test.name)

			for test_run in self.test_runs:
				configuration = doc.createElement('configuration')
				configuration.setAttribute('result', test_run['results'][test.name])

				for k, v in test_run['configuration'].iteritems():
					if k != '':
						option = doc.createElement('option')
						option.setAttribute('name', k)
						value  = doc.createTextNode(v)
						option.appendChild(value)
						configuration.appendChild(option)

				test_node.appendChild(configuration)

			root.appendChild(test_node)

		return doc.toxml()
