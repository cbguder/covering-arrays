#!/usr/bin/env python

from xml.dom.minidom import Document
from xml.dom.minidom import parse as _parse

class ConfigurationModel:
	def __init__(self):
		self.options = []

	@staticmethod
	def from_xml(xml_file):
		model   = ConfigurationModel()
		dom     = _parse(xml_file)
		options = dom.getElementsByTagName('option')

		for option_node in options:
			model.options.append(Option.from_node(option_node))
		dom.unlink()

		return model		

	def to_xml(self):
		doc = Document()
		root = doc.createElement('options')
		doc.appendChild(root)

		for option in self.options:
			option_node = doc.createElement('option')
			option_node.setAttribute('name', option.name)

			for value in option.values:
				value_node = doc.createElement('value')
				value_node.appendChild(doc.createTextNode(str(value)))

				option_node.appendChild(value_node)

			root.appendChild(option_node)

		return doc.toxml()

class Option:
	def __init__(self, name):
		self.name   = name
		self.values = []

	@staticmethod
	def from_node(node):
		option = Option(node.getAttribute('name'))
		values = node.getElementsByTagName('value')

		for value in values:
			option.values.append(value.firstChild.nodeValue)

		return option
