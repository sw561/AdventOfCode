#!/usr/bin/env python3

def read(fname):
	instructions = dict()
	with open(fname, 'r') as f:
		for line in f:
			u = [x.strip() for x in line.replace('>', '').split('-')]
			instructions[u[1]] = u[0]
	return instructions

funcs = dict()
def add_to_funcs(f):
	funcs[f.__name__] = f

@add_to_funcs
def NOT(x):
	return ((1<<16) - 1) ^ x

@add_to_funcs
def AND(x, y):
	return x & y

@add_to_funcs
def OR(x, y):
	return x | y

@add_to_funcs
def LSHIFT(x, y):
	return x << y

@add_to_funcs
def RSHIFT(x, y):
	return x >> y

def circuit(to_find, instructions):
	def circuit_(to_find):
		# print("Calling circuit with to_find = {}".format(to_find))
		try:
			u = instructions[to_find]
		except KeyError:
			return int(to_find)

		if type(u) is int:
			return u

		x = u.split()
		if len(x) == 1:
			ret = circuit_(x[0])

		elif len(x) == 2:
			ret = funcs[x[0]](circuit_(x[1]))

		elif len(x) == 3:
			ret = funcs[x[1]](circuit_(x[0]), circuit_(x[2]))

		instructions[to_find] = ret
		return ret
	return circuit_(to_find)

if __name__=="__main__":
	import sys

	instructions = read(sys.argv[1])
	instructions_copy = dict(instructions)

	a = circuit(sys.argv[2], instructions)
	print("Part 1: {}: {}".format(sys.argv[2], a))

	# Part 2
	instructions_copy['b'] = a
	print("Part 2: {}: {}".format(sys.argv[2], circuit(sys.argv[2], instructions_copy)))
