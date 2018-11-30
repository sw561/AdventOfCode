#!/usr/bin/env python3

from math import sqrt
import numpy as np

def factors(x):
	top = sqrt(x)
	i = 1
	while i < top:
		if not x%i:
			yield i
			yield x//i
		i += 1

	if abs(int(top) - top) < 1e-5:
		yield int(top)

def n_presents(x):
	return 10*sum(factor for factor in factors(x))

if __name__=="__main__":
	s = 29000000

	# Upper bound is s//10, we know n_presents at s//10 must be larger than s
	print("n_presents(s//10):", n_presents(s//10))

	# Part 1
	u = np.ones(s//10 + 1, dtype=int)
	for elf in range(2, len(u)):
		u[elf::elf] += elf
	u *= 10

	for i, x in enumerate(u[1:10], 1):
		print("House {} got {} = {} presents.".format(i, x, n_presents(i)))

	for i, x in enumerate(u[1:], 1):
		if x >= s:
			print("Part 1:", i)
			print(n_presents(i))
			break

	# Part 2
	u = np.ones(s//10 + 1, dtype=int)
	for elf in range(2, len(u)):
		u[elf:51*elf:elf] += elf
	u *= 11

	for i, x in enumerate(u[1:], 1):
		if x >= s:
			print("Part 2:", i)
			print(n_presents(i))
			break
