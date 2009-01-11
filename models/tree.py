#!/usr/bin/env python

import re
from xml.dom.minidom import Document

class DecisionTree:
	def __init__(self):
		self.children = []

	def classify(self, configuration):
		for c in self.children:
			r = c.classify(configuration)
			if r != None:
				return r
		return None

	def to_xml(self):
		doc  = Document()
		root = doc.createElement('decisiontree')

		for child in self.children:
			root.appendChild(child.to_xml_node(doc))
		doc.appendChild(root)

		return doc.toxml()

	def from_file(file):
		lines = [line.strip() for line in file]

		tree = find_j48(lines)
		if tree == None:
			return None

		dtree = DecisionTree()
		node  = dtree
		stack = [dtree]

		for line in tree:
			m = re.match("""(\|   )*(\w+) (\S+) (\w+)(: (\w+))?""", line)
			if m != None:
				level = 0
				result = None
				if m.group(1) != None:
					level = len(m.group(1)) / 4
				option   = m.group(2)
				operator = m.group(3)
				value    = int(m.group(4))
				if m.group(5) != None:
					result = m.group(6)
				parent = None

				if level < len(stack) - 1:
					stack.pop()
				elif level > len(stack) - 1:
					stack.append(node)

				node = DecisionTreeNode(option, operator, int(value), result)
				stack[-1].children.append(node)

		return dtree
	from_file = staticmethod(from_file)

class DecisionTreeNode:
	def __init__(self, option, operator, value, result = None):
		self.option   = option
		self.operator = operator
		self.value    = value
		self.result   = result
		self.children = []

		if self.operator == '=':
			self.operator = '=='

	def classify(self, configuration):
		if eval('%s %s %s' % (configuration[self.option], self.operator, self.value)):
			if self.result != None:
				return self.result
			else:
				for c in self.children:
					r = c.classify(configuration)
					if r != None:
						return r
		return None

	def to_xml_node(self, doc):
		node = doc.createElement('test')
		node.setAttribute('attribute', self.option)
		node.setAttribute('operator',  self.operator)
		node.setAttribute('value',     str(self.value))

		if self.result == None:
			for child in self.children:
				node.appendChild(child.to_xml_node(doc))
		else:
			output = doc.createElement('output')
			output.setAttribute('result', self.result)
			node.appendChild(output)

		return node

def find_j48(lines):
	start = end = None
	for i in range(len(lines)):
		line = lines[i]
		if line == 'J48 pruned tree':
			start = i + 3
		elif start != None and line == '' and i > start:
			end = i
			return lines[start:end]
	return None

def determine_level(line):
	level = 0
	while line.startswith('|   '):
		level += 1
		line = line[4:]
	return level
