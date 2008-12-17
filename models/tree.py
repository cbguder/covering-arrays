#!/usr/bin/env python

class DecisionTree:
	def __init__(self):
		self.children = []
	
	def classify(self, configuration):
		for c in self.children:
			r = c.classify(configuration)
			if r != None:
				return r
		return None

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
