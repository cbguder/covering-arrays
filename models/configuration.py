#!/usr/bin/env python

from xml.dom.minidom import parse

class ConfigurationModel:
	def __init__(self):
		self.options = []

	def from_xml(xml_file):
		model   = ConfigurationModel()
		dom     = parse(xml_file)
		options = dom.getElementsByTagName('option')

		for option_node in options:
			model.options.append(Option(option_node))
		dom.unlink()

		return model		
	from_xml = staticmethod(from_xml)

class Option:
	def __init__(self, node):
		self.name   = node.attributes.item(0).nodeValue
		self.values = []

		values = node.getElementsByTagName('value')
		for value in values:
			self.values.append(value.firstChild.nodeValue)
