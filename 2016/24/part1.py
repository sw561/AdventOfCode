#!/usr/bin/env python3

from itertools import permutations
import sys

PART2 = False

def make_grid(f):
	grid = []
	for line in open(f, 'r'):
		grid.append(list(line.strip()))

	return grid

def print_grid(g):
	print("\n".join("".join(row) for row in g))

def neighbours(g, pos):
	# Find neighbours which aren't a wall
	for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		p = (pos[0] + rd, pos[1] + cd)
		if g[p[0]][p[1]]!='#':
			yield p

def route_find(g, start):
	distances = dict()

	visited = set()
	visited.add(start)

	d = 1
	stack = [start]
	new_stack = []

	while stack or new_stack:
		if not stack:
			stack, new_stack = new_stack, stack
			d += 1

		for n in neighbours(g, stack.pop()):
			if n in visited:
				continue

			new_stack.append(n)
			visited.add(n)

			x = g[n[0]][n[1]]
			if x != '.' and int(x) not in distances:
				distances[int(x)] = d

	return distances

def salesman_distances(distance_matrix):
	# Distance from i to j is distance_matrix[i][j]

	# Given start at 0
	for p in permutations(range(1, 1+max(distance_matrix.keys()))):
		pos = 0
		d = 0

		for pi in p:
			d += distance_matrix[pos][pi]
			pos = pi

		# ---------- For part 2 ---------- #
		if PART2:
			d += distance_matrix[pos][0]

		yield d

def salesman(distance_matrix):
	return min(salesman_distances(distance_matrix))

def main():
	g = make_grid(sys.argv[1])

	positions = dict()
	for r, row in enumerate(g):
		for c, x in enumerate(row):
			if x not in ['#', '.']:
				positions[int(x)] = (r, c)

	print(positions)

	distance_matrix = dict()

	for n, p in positions.items():
		distance_matrix[n] = route_find(g, p)

	for n, k in distance_matrix.items():
		print("{}: {}".format(n, k))

	print("Part 1: {}".format(salesman(distance_matrix)))

	global PART2
	PART2 = True
	print("Part 2: {}".format(salesman(distance_matrix)))

if __name__=="__main__":
	main()
