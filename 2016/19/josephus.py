#!/usr/bin/env python3

from math import log, floor

# n people sit in a circle
# The first person kills the person to their left it will be the third person's
# go.
# Continue until only one is left.
#
# If there are 2^x people left, the person whose go it is wins.
# If n starts at 2^x + b then b goes will pass until there are 2^x people left.
# After b goes, it will be the turn of 2*b + 1

def josephus(x):
	# Remove highest power of 2, multiply by 2 and add 1.
	# This is equivalent to removing most significant binary digit and
	# appending a 1.

	a = bin(x)
	a = a[3:]+'1'
	a = int(a, 2)
	return a

def simulate_josephus_circular(x):
	q = list(range(1, x+1))
	t = -1 # Index of elf whose turn it is
	target = -1
	removed = -1 # Start off uninitialised
	while q:
		if target < t:
			# t now points to the next one already
			t = t % len(q)
		else:
			t = (t+1) % len(q)

		target = (t+len(q)//2) % len(q)
		removed = q[target]
		# print(q, q[t], removed)
		if len(q)%1000==0: print("Making progress... len(q)={}".format(len(q)))
		q.pop(target)
	return removed

# Points where sim(x) returns x are s.t. x = 3**n
# Then start counting from one. Add one until x = 2*i.
# So transition point is 2*x -> x
# Above 2*x go count in increments of 2
def josephus_circular(x):
	n = floor(log(x, 3))
	u = pow(3, n)
	transition = 2*u
	if x==u:
		return u
	if x<transition:
		# Counting in increments of 1
		return x-u
	elif x>=transition:
		return transition//2 + 2*(x-transition)

print(josephus(5))
print(josephus(41))

puzzle = 3017957

# Part 1
print(josephus(puzzle))

# Experimenting for part 2
# for i in range(1,100):
# 	print(i, simulate_josephus_circular(i), josephus_circular(i))

# Part 2
print(josephus_circular(puzzle))

# This works too, but takes a good while
# print(simulate_josephus_circular(3017957))
