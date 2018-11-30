#!/usr/bin/env python3

from itertools import permutations

def add(d, a, b, distance):
	if a not in d:
		d[a] = dict()
	d[a][b] = distance

def read(fname):
	distances = dict()
	with open(fname, 'r') as f:
		for line in f:
			u = line.split()
			name = u[0]
			h = int(u[3])
			if u[2] == "lose":
				h *= -1
			neighbour = u[-1][:-1]
			add(distances, name, neighbour, h)

	return distances

def table_permutations(x):
	# Symmetry of circular table means mirror images are the same, and
	# rotations are the same.
	#
	# x is list of distinct elements.

	# This means we can choose an arbitrary element of x and place it first.
	# We can then eliminate mirror images reflected around x by placing the
	# restriction that the element to the left of x, is larger than the elment
	# to the right of x. By larger we can mean anything, so just use relative
	# positions in the list x.

	u = [None]*3
	u[1] = x[0]
	for second_index in range(1, len(x)):
		u[0] = x[second_index]
		for third_index in range(second_index+1, len(x)):
			u[2] = x[third_index]
			for p in permutations(x[i] for i in\
					range(1, len(x)) if i not in [second_index, third_index]):
				yield u + list(p)

def pairs(x):
	# Yield all adjacent pairs given a list x, including x[0], x[-1]
	yield from zip(x, x[1:])
	yield x[-1], x[0]

def main(distances):
	def happiness(x):
		return sum(distances[a][b] + distances[b][a] for a, b in pairs(x))

	best = max(table_permutations(list(distances.keys())), key=happiness)
	val = happiness(best)
	return best, val

if __name__=="__main__":
	import sys

	distances = read(sys.argv[1])

	# Part 1
	best, val = main(distances)
	print("Part 1: {} {}".format(best, val))

	# Part 2

	distances["Simon"] = dict()
	for name in distances:
		distances["Simon"][name] = 0
		distances[name]["Simon"] = 0

	best, val = main(distances)
	print("Part 2: {} {}".format(best, val))
