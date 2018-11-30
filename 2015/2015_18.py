#!/usr/bin/env python3

from copy import deepcopy
import sys

def r(x):
	if x=='#': return 1
	elif x=='.': return 0
	else:
		raise Exception("Not good", x)

def s(x):
	if x==1: return '#'
	elif x==0: return '.'
	else:
		raise Exception("Wow", x)

def read(fname):
	with open(fname, 'r') as f:
		data = [[r(i) for i in line.strip()] for line in f]
	return data

def p(data):
	print("\n".join("".join(s(u) for u in row) for row in data))
	print("---------")

def neighbours(i, j, n):
	for dx in range(-1, 2):
		x = i+dx
		if 0 <= x < n:
			for dy in range(-1, 2):
				if dx == dy == 0: continue
				y = j+dy
				if 0 <= y < n:
					yield (x, y)

def update(u, u2):
	for i in range(len(u)):
		for j in range(len(u)):
			n_neighbours = sum(1 for x, y in neighbours(i, j, len(u)) if u[x][y])

			if n_neighbours == 3 or (n_neighbours == 2 and u[i][j]):
				u2[i][j] = 1
			else:
				u2[i][j] = 0

def main(part2=False):
	data = read(sys.argv[1])

	if part2:
		for i in [0, len(data)-1]:
			for j in [0, len(data)-1]:
				data[i][j] = 1

	data2 = deepcopy(data)
	# p(data)

	# Part 1
	for i in range(int(sys.argv[2])):
		update(data, data2)
		data2, data = data, data2
		if part2:
			for i in [0, len(data)-1]:
				for j in [0, len(data)-1]:
					data[i][j] = 1
		# p(data)

	return sum(sum(x) for x in data)

if __name__=="__main__":

	print("Part 1:", main())
	print("Part 2:", main(part2=True))
