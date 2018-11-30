#!/usr/bin/env python

from triangle import possible

def get_input_3():
	while True:
		three = []
		try:
			for i in xrange(3):
				three.append(map(int, raw_input().split()))
			yield three
		except EOFError:
			return

def get_triangles():
	for three in get_input_3():
		for col in xrange(3):
			yield [row[col] for row in three]

if __name__=="__main__":
	# Part 2
	print sum(1 for sides in get_triangles() if possible(sides))
