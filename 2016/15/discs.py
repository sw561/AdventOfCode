#!/usr/bin/env python3

class Disc(object):
	def __init__(self, n, npos, pos):
		self.n = n
		self.npos = npos
		self.pos = pos

	def slot(self, t):
		# If the ball is dropped at time t, it will reach disc n at time t+n
		# At time t+n it has rotated t+n positions from its starting position
		new_pos = (self.pos + t + self.n) % self.npos
		# Return true if in position of slot
		return new_pos==0

def get_input():
	while True:
		try:
			x = input()
			x = x.split()
			n = int(x[1][1:])
			npos = int(x[3])
			pos = int(x[11][:-1])
			yield Disc(n, npos, pos)
		except EOFError:
			return

def solve(discs, nmax=int(1e8)):
	# Find first drop time for which all slots will be open
	for i in range(nmax):
		if all(d.slot(i) for d in discs):
			return i
	raise Exception("Did not find any good drop time, nmax={}".format(i))

discs = [d for d in get_input()]

# Part 1
print(solve(discs))

# Part 2
discs.append(Disc(discs[-1].n+1, 11, 0))
print(solve(discs))
