#!/usr/bin/env python3

def read(fname):
	with open(fname, 'r') as f:
		return f.read().strip()

def update_coords(coords, i):
	if i=='^':
		coords = coords[0], coords[1] + 1
	elif i=='v':
		coords = coords[0], coords[1] - 1
	elif i=='>':
		coords = coords[0] + 1, coords[1]
	elif i=='<':
		coords = coords[0] - 1, coords[1]
	return coords

def main(data, part2=False):
	visited = set()
	coords = (0, 0)
	robo = (0, 0)
	visited.add(coords)

	for step, i in enumerate(data):
		if step%2 or not part2:
			coords = update_coords(coords, i)
			visited.add(coords)
		else:
			robo = update_coords(robo, i)
			visited.add(robo)

	print("Part {}: {}".format(2 if part2 else 1, len(visited)))

if __name__=="__main__":
	import sys

	data = read(sys.argv[1])

	main(data)
	main(data, part2=True)
