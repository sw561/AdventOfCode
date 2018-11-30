#!/usr/bin/env python3

def read(fname):
	with open(fname, 'r') as f:
		for line in f:
			d = dict()
			for ui in line.split(','):
				x = ui.split()
				prop = x[-2].strip()[:-1]
				n = int(x[-1])
				d[prop] = n

			yield d

def valid(measurement, candidate):
	return all(candidate[key] == measurement[key] for key in candidate)

def satisfies(key, m, c):
	if key in ["cats", "trees"]:
		return c > m
	elif key in ["pomerians", "goldfish"]:
		return c < m
	else:
		return c == m

def valid_part2(measurement, candidate):
	return all(satisfies(key, measurement[key], candidate[key]) for key in candidate)

if __name__=="__main__":

	measurement = {
		"children": 3,
		"cats": 7,
		"samoyeds": 2,
		"pomeranians": 3,
		"akitas": 0,
		"vizslas": 0,
		"goldfish": 5,
		"trees": 3,
		"cars": 2,
		"perfumes": 1,
	}

	import sys

	for i, sue in enumerate(read(sys.argv[1]), 1):
		if valid(measurement, sue):
			print("Part 1: i, sue:", i, sue)
		if valid_part2(measurement, sue):
			print("Part 2: i, sue:", i, sue)
