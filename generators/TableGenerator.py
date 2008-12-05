#!/usr/bin/env python

class TableGenerator:
	def __init__(self):
		self.__init__(None, None)

	def __init__(self, options, tests, test_runs):
		self.options   = options
		self.tests     = tests
		self.test_runs = test_runs
	
	def generate(self):
		return self.array_to_ascii_table(self.generate_table())

	def generate_table(self):
		table = []

		h_options = [option.name for option in self.options]
		h_tests   = [test.name for test in self.tests]

		header = h_options + h_tests
		table.append(header)

		for test_run in self.test_runs:
			row = []
			for option in h_options:
				row.append(test_run['configuration'][option])
			for test in h_tests:
				row.append(test_run['results'][test])
			table.append(row)

		return table

	def array_to_ascii_table(table):
		output = []
		num_columns   = len(table[0])
		column_widths = [max([len(row[i]) for row in table]) for i in range(num_columns)]
	
		separator = '+-' + '-+-'.join(['-'*column_widths[i] for i in range(num_columns)]) + '-+'
	
		for row in table:
			line =  '| ' + ' | '.join([row[i].ljust(column_widths[i]) for i in range(num_columns)]) + ' |'
			output.append(line)
	
		output.insert(0, separator)
		output.insert(2, separator)
		output.append(separator)
	
		return '\n'.join(output)
	array_to_ascii_table = staticmethod(array_to_ascii_table)
