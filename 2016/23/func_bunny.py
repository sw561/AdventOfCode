#!/usr/bin/env python3

import numpy as np

actions = dict()
memory = dict((i, 0) for i in "abcd")
n = 0

def clear_memory():
	for i in memory:
		memory[i] = 0

def action(f):
	actions[f.__name__] = f

def interpret(x):
	# Parse a thing x which may be a number or may refer to a register
	try:
		return memory[x]
	except KeyError:
		return int(x)

@action
def inc(code_pointer, key):
	memory[key] += 1
	return code_pointer + 1

@action
def dec(code_pointer, key):
	memory[key] -= 1
	return code_pointer + 1

@action
def cpy(code_pointer, x, y):
	memory[y] = interpret(x)
	return code_pointer + 1

@action
def jnz(code_pointer, x, y):
	print("{:3d} {}".format(code_pointer,
		" ".join("{:8d}".format(i) for key, i in sorted(memory.items()))
		))
	if interpret(x):
		return code_pointer + interpret(y)
	return code_pointer + 1

@action
def tgl(code_pointer, x):
	toggled = True
	try:
		c = code[code_pointer + interpret(x)]
	except IndexError:
		c = []
	if len(c)==2:
		c[0] = "dec" if c[0]=="inc" else "inc"
	elif len(c)==3:
		c[0] = "cpy" if c[0]=="jnz" else "jnz"
	else:
		print("Could not toggle")
		toggled = False
	if toggled:
		for i in code:
			print(" ".join(j for j in i))
		print("-----")
	return code_pointer + 1

# mul a b c : write (a*b) into register c
@action
def mul(code_pointer, a, b, c):
	memory[c] = interpret(a) * interpret(b)
	return code_pointer + 1

@action
def add(code_pointer, a, b, c):
	memory[c] = interpret(a) + interpret(b)
	return code_pointer + 1

def run():
	code_pointer = 0
	clear_memory()

	global n
	while code_pointer < len(code):
		n += 1
		# if n > 100: exit("AAAA")
		q = code[code_pointer]
		code_pointer = actions[q[0]](code_pointer, *q[1:])

def print_memory():
	for key, i in sorted(memory.items()):
		print("{}: {}".format(key, i))

if __name__=="__main__":
	import sys
	fname = sys.argv[1]
	code = [line.strip().split() for line in open(fname, 'r')]
	run()
	print_memory()
