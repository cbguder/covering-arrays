#!/usr/bin/env python

from xml.dom.minidom import parse

class ConfigurationModel:
	def __init__(self, xml_file):
		self.options = []

		dom = parse(xml_file)
		options = dom.getElementsByTagName('option')
		for option_node in options:
			self.options.append(Option(option_node))
		dom.unlink()

class Option:
	def __init__(self, node):
		self.name   = node.attributes.item(0).nodeValue
		self.values = []

		values = node.getElementsByTagName('value')
		for value in values:
			self.values.append(value.firstChild.nodeValue)
