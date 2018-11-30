#!/usr/bin/env python3

from itertools import permutations, chain

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

def happiness(x, distances):
	return sum(distances[origin][destination] + distances[destination][origin] for\
		origin, destination in x)

def main(distances):
	first_name = next(iter(distances))
	others = (u for u in distances.keys() if u != first_name)

	def add_first(x):
		return zip(chain([first_name], x), chain(x, [first_name]))

	def happ(x):
		return happiness(add_first(x), distances)

	best = max(permutations(others), key=happ)
	val = happ(best)
	best = [first_name] + list(best)
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
