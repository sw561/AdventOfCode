#!/usr/bin/env python3

from itertools import combinations
from functools import reduce

def product(it):
	return reduce(lambda x, y: x*y, it)

def wrapping_paper(dimensions):
	sides = [product(it) for it in combinations(dimensions, 2)]
	return 2*sum(sides) + min(sides)

def ribbon(dimensions):
	to_wrap = 2*(sum(dimensions) - max(dimensions))
	bow = product(dimensions)
	return to_wrap + bow

def read(fname):
	data = []
	with open(fname, 'r') as f:
		for line in f:
			data.append([int(x) for x in line.strip().split('x')])
	return data

if __name__=="__main__":
	import sys

	data = read(sys.argv[1])

	total_area = sum(wrapping_paper(i) for i in data)
	print("Part 1:", total_area)

	total_ribbon = sum(ribbon(i) for i in data)
	print("Part 2:", total_ribbon)
