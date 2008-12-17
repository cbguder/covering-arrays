#!/usr/bin/env python

import re
import sys
from models import DecisionTree, DecisionTreeNode

def main(file):
	f = open(file)
	lines = [line.strip() for line in f]
	f.close()
	dtree = parse_j48(lines)

def parse_j48(input):
	tree = find_j48(input)
	if tree == None:
		print "ERROR: Can't find tree"
		sys.exit()
	
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

def find_j48(input):
	start = end = None
	for i in range(len(input)):
		line = input[i]
		if line == 'J48 pruned tree':
			start = i + 3
		elif start != None and line == '' and i > start:
			end = i
			return input[start:end]
	return None

def determine_level(line):
	level = 0
	while line.startswith('|   '):
		level += 1
		line = line[4:]
	return level

if __name__ == '__main__':
	main(sys.argv[1])