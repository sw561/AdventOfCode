#!/usr/bin/env python3

class Program(object):
	def __init__(self, code):
		self.code = code
		self.position = 0
		self.memory = dict()
		for register in ['a','b','c','d']:
			self.memory[register] = 0

	def run(self, debug=False):
		while self.position < len(self.code):
			if debug:
				print("Log: calling {}".format(self.code[self.position]))
			for k in self.preprocessor(self.code[self.position]):
				if debug:
					print("Log: calling from PreProcessor {}".format(k))
				self.call(k)
			self.position += 1

	def run_output(self, debug=False):
		self.code.append("for_all print".split())
		self.run(debug)

	def preprocessor(self, instruction):
		if instruction[0] == "inc":
			yield "add {} 1".format(instruction[1]).split()
		elif instruction[0] == "dec":
			yield "add {} -1".format(instruction[1]).split()
		elif instruction[0] == "for_all":
			yield from self.for_all(instruction[1:])
		else:
			yield instruction

	def for_all(self, instruction):
		if instruction[0]=="cpy":
			val = self.get_value(instruction[1])
			for register in sorted(self.memory):
				yield "cpy {} {}".format(val, register).split()
		elif instruction[0]=="print":
			for register in sorted(self.memory):
				yield "print {0} %{0}".format(register).split()
		else:
			raise Exception("for_all not supported for '{}'".format(instruction))

	def call(self, instruction):
		if instruction[0]=="cpy":
			self.copy(instruction[1], instruction[2])
		elif instruction[0]=="add":
			self.add(instruction[1], instruction[2])
		elif instruction[0]=="jnz":
			self.jnz(instruction[1], instruction[2])
		elif instruction[0]=="print":
			self.assembunny_print(instruction[1:])
		else:
			raise Exception("Syntax Error in assembunny -> {}".\
				format(" ".join(instruction)))

	def get_value(self, x):
		# x can be a number or a register
		try:
			value = int(x)
		except ValueError:
			value = self.memory[x]
		return value

	def copy(self, origin, destination):
		value = self.get_value(origin)
		self.memory[destination] = value

	def add(self, register, x):
		self.memory[register] += self.get_value(x)

	def jnz(self, condition, jump):
		if self.get_value(condition):
			# Minus one to compensate for usual stepping through code
			self.position += self.get_value(jump) - 1

	def get_value_string(self, x):
		if x[0]=='%':
			return str(self.get_value(x[1:]))
		else:
			return x

	def assembunny_print(self, instructions):
		print(" ".join(self.get_value_string(i) for i in instructions))

if __name__=="__main__":
	import sys
	fname = sys.argv[1]
	p = Program([line.strip().split() for line in open(fname, 'r')])
	p.run(sys.argv[2:])
