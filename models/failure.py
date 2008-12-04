#!/usr/bin/env python

from xml.dom.minidom import parse

class FailureModel:
	def __init__(self, xml_file):
		self.tests = []

		dom = parse(xml_file)
		tests = dom.getElementsByTagName('test')
		for test in tests:
			self.tests.append(Test(test))
		dom.unlink()

class Test:
	def __init__(self, node):
		self.name     = node.attributes.item(0).nodeValue
		self.patterns = []

		patterns = node.getElementsByTagName('pattern')
		for pattern in patterns:
			self.patterns.append(FailurePattern(pattern))

	def run_with_configuration(self, configuration):
		# TODO: What if it holds for more than one pattern?
		for pattern in self.patterns:
			all_hold = True
			for name, value in pattern.options.iteritems():
				if configuration[name] != value:
					all_hold = False
					break
			if all_hold:
				return pattern.result
		return 'p'

class FailurePattern:
	def __init__(self, node):
		self.result  = node.attributes.item(0).nodeValue
		self.options = {}

		options = node.getElementsByTagName('option')
		for option in options:
			name  = option.attributes.item(0).nodeValue
			value = option.firstChild.nodeValue
			self.options[name] = value
