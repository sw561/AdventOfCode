#!/usr/bin/env python

# Follow directions in a taxicab geometry.
#
# Each direction is of the form Xn where X is L or R and indicates the
# direction to turn, n is the number of blocks to walk.
#
# Start facing North.

from math import pi, sin, cos

def direction(angle):
	return map(int, map(round, [cos(angle), sin(angle)]))

def follow(turns):
	pos = [0, 0] # x, y Cartesian geometry
	angle = pi/2 # Normal polar coords

	visited_squares = set()
	visited_squares.add(tuple(pos))
	find_first_repeated = True

	for i in turns:
		if i[0]=='R':
			# Turn right
			angle -= pi/2
		elif i[0]=='L':
			angle += pi/2

		d = direction(angle)

		x = int(i[1:])

		for step in xrange(1, x+1):
			for c in [0,1]:
				pos[c] += d[c]

			elem = tuple(pos)
			if find_first_repeated:
				if elem in visited_squares:
					print "Found repeated"
					print sum(abs(x) for x in elem)
					find_first_repeated = False
				else:
					visited_squares.add(elem)

	return sum(abs(x) for x in pos)

if __name__=="__main__":
	turns = [i.strip() for i in raw_input().split(',')]

	print follow(turns)
