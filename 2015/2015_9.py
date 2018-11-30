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
			u = line.split('=')
			a, _, b = u[0].split()
			d = int(u[1])

			add(distances, a, b, d)
			add(distances, b, a, d)

	return distances

def distance(route, distances):
	return sum(distances[origin][destination] for\
		origin, destination in zip(route, route[1:]))

def fastrange(n, i, j):
	# Yield numbers up to n, excluding i and j
	# This way does the fewest comparisons possible
	yield from range(i)
	yield from range(i+1, j)
	yield from range(j+1, n)

def routes(places):
	# Find routes going through all places. Given that the return route is
	# considered equivalent, we can assume the order of the first and last
	# visited place.

	for i in range(len(places)):
		for j in range(i+1, len(places)):
			for p in permutations(places[k] for k in\
					fastrange(len(places), i, j)):
				yield [places[i]] + list(p) + [places[j]]

if __name__=="__main__":
	import sys

	distances = read(sys.argv[1])

	# Get shortest and longest at the same time
	g = routes(list(distances.keys()))
	x = next(g)
	shortest = distance(x, distances)
	longest = shortest

	for x in g:
		d = distance(x, distances)
		if d < shortest:
			shortest = d
		elif d > longest:
			longest = d

	print("Part 1:", shortest)
	print("Part 2:", longest)
