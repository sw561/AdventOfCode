#!/usr/bin/env python

# Deterine if the triangles are possible or not given three side lengths

def possible(sides):
	s = sum(sides)
	m = max(sides)
	return m<s-m

def get_input():
	while True:
		try:
			yield map(int, raw_input().split())
		except EOFError:
			return

if __name__=="__main__":
	# Part 1
	print sum(1 for sides in get_input() if possible(sides))
