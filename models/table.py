#!/usr/bin/env python

class Table:
	def __init__(self):
		self.options   = []
		self.tests     = []
		self.errors    = {}
		self.test_runs = []

	@staticmethod
	def from_file(file):
		def get_parts(str):
			parts = str.split('|')
			parts = [p.strip() for p in parts if p != '']
			return parts

		table = Table()

		f = open(file)
		lines = f.readlines()
		f.close()

		header = get_parts(lines[1])

		for p in header:
			if p.startswith('o'):
				table.options.append(p)
			elif p.startswith('t'):
				table.tests.append(p)

		for test in table.tests:
			table.errors[test] = []

		l_options = len(table.options)
		l_tests   = len(table.tests)

		for line in lines[3:-1]:
			test_run = { 'configuration': {}, 'results': {} }
			parts = get_parts(line)

			for i in range(l_options):
				test_run['configuration'][table.options[i]] = parts[i]

			for i in range(l_tests):
				result = parts[l_options+i]
				test_run['results'][table.tests[i]] = result
				if result != 'p' and result not in table.errors[table.tests[i]]:
					table.errors[table.tests[i]].append(result)

			table.test_runs.append(test_run)

		return table
