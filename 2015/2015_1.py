#!/usr/bin/env python3

def main(u):
	floor = 0
	part2_done = False
	for i, x in enumerate(u, 1):
		if x == '(':
			floor += 1
		elif x == ')':
			floor -= 1

		if floor == -1 and not part2_done:
			part2_result = i
			part2_done = True

	print("Part 1:", floor)
	print("Part 2:", part2_result)

def read(fname):
	with open(fname, 'r') as f:
		u = f.read().strip()
	return u

if __name__=="__main__":
	import sys

	main(read(sys.argv[1]))
