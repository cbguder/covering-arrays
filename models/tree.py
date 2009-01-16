#!/usr/bin/env python

import re
from xml.dom.minidom import Document

class DecisionForest:
	def __init__(self):
		self.trees = []

	def to_xml(self):
		doc  = Document()
		root = doc.createElement('forest')

		for tree in self.trees:
			root.appendChild(tree.to_xml_node(doc))
		doc.appendChild(root)

		return doc.toxml()

class DecisionTree:
	def __init__(self):
		self.children = []
		self.test     = None
		self.error    = None
		self.result   = None

	def classify(self, configuration):
		for c in self.children:
			r = c.classify(configuration)
			if r != None:
				return r
		return None

	def to_xml_node(self, doc):
		root = doc.createElement('tree')
		root.setAttribute('test',  self.test)
		root.setAttribute('error', self.error)

		if self.result:
			output = doc.createElement('output')
			output.setAttribute('result', self.result)
			root.appendChild(output)

		for child in self.children:
			root.appendChild(child.to_xml_node(doc))
		doc.appendChild(root)

		return root

	@staticmethod
	def from_file(file):
		lines = [line.strip() for line in file]

		tree = find_j48(lines)
		if tree == None:
			return None

		dtree = DecisionTree()
		node  = dtree
		stack = [dtree]

		for line in tree:
			m = re.match(""": (\w+)""", line)
			if m != None:
				dtree.result = m.group(1)
				return dtree

			m = re.match("""(\|   )*(\w+) (\S+) (\w+)(: (\w+))?""", line)
			if m != None:
				level = 0
				result = None

				if m.group(1) != None:
					level = m.start(2) / 4

				option   = m.group(2)
				operator = m.group(3)
				value    = int(m.group(4))

				if m.group(5) != None:
					result = m.group(6)

				node = DecisionTreeNode(option, operator, int(value), result)
				stack[level].children.append(node)

				if level + 2 > len(stack):
					stack.append(node)
				else:
					stack[level + 1] = node

		return dtree

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
	for i, line in enumerate(lines):
		if line == 'J48 pruned tree':
			if lines[i+2] == '':
				start = i + 3
			else:
				start = i + 2
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
