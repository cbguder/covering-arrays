#!/usr/bin/env python

import random
from xml.dom.minidom import Document, parse

class FailureModel:
	def __init__(self):
		self.tests = []

	def from_xml(xml_file):
		model = FailureModel()
		dom   = parse(xml_file)
		tests = dom.getElementsByTagName('test')

		for test in tests:
			model.tests.append(Test.from_node(test))
		dom.unlink()

		return model
	from_xml = staticmethod(from_xml)

	def to_xml(self):
		doc = Document()
		root = doc.createElement('patterns')
		doc.appendChild(root)

		for test in self.tests:
			test_node = doc.createElement('test')
			test_node.setAttribute('name', test.name)

			for pattern in test.patterns:
				pattern_node = doc.createElement('pattern')
				pattern_node.setAttribute('result', pattern.result)

				for k,v in pattern.options.iteritems():
					option_node = doc.createElement('option')
					option_node.setAttribute('name', k)
					option_node.appendChild(doc.createTextNode(v))

					pattern_node.appendChild(option_node)

				test_node.appendChild(pattern_node)

			root.appendChild(test_node)

		return doc.toxml()

class Test:
	def __init__(self):
		self.name     = ''
		self.patterns = []

	def from_node(node):
		test = Test()
		test.name = node.getAttribute('name')

		patterns = node.getElementsByTagName('pattern')
		for pattern in patterns:
			test.patterns.append(FailurePattern.from_node(pattern))

		return test
	from_node = staticmethod(from_node)

	def run_with_configuration(self, configuration):
		# TODO: What if it holds for more than one pattern?
		for pattern in self.patterns:
			all_hold = True
			for name, value in pattern.options.iteritems():
				if configuration[name] != value:
					all_hold = False
					break
			if all_hold and random.random() < pattern.probability:
				return pattern.result
		return 'p'

class FailurePattern:
	def __init__(self):
		self.result      = ''
		self.probability = 1.0
		self.options     = {}

	def from_node(node):
		pattern = FailurePattern()
		pattern.result      = node.getAttribute('result')
		pattern.probability = node.getAttribute('probability')
		try:
			pattern.probability = float(pattern.probability)
		except:
			pattern.probability = 1.0

		options = node.getElementsByTagName('option')
		for option in options:
			name  = option.getAttribute('name')
			value = option.firstChild.nodeValue
			pattern.options[name] = value

		return pattern
	from_node = staticmethod(from_node)
