#!/usr/bin/env python3

# Define state as a list of length 16, where each index represents a state. A
# state consists of a location for the generator and a location of the
# microchip. Since each location can be one of four possible floors, there are
# 16 possible states.
# The value in the list is the number of generator chip pairs in that state.

# We will make moves, excluding moves which will lead to fried microchips and
# excluding moves which go back to previously visited states and continue until
# we find the state we are looking for.

# The state index//4 gives the floor of the RTG (=generator) (zero-indexed FTW)
# The state index%4 gives the floor of the microchip
# A microchip is with its RTG if its index%5==0
# i.e. if index is [0->(0,0), 5->(1,1), 10->(2,2), 15->(3,3)]

from string import ascii_uppercase, ascii_lowercase

NFLOORS = 4

def RTG(index):
	return index // NFLOORS

def microchip(index):
	return index % NFLOORS

def chip_with_generator(index):
	return not index % (NFLOORS+1)

class State(object):
	def __init__(self, orig=None):
		if orig is not None:
			# Copy data, not just the reference
			self.data = orig.data[:]
			self.elevator = orig.elevator
		else:
			# This is the default list of length nfloors^2
			self.data = [0]*(NFLOORS**2)
			self.elevator = 0

	def __eq__(self, other):
		# This method is required to make states hashable
		if self.elevator != other.elevator:
			return False
		if self.data != other.data:
			return False
		return True

	def __hash__(self):
		return hash((self.elevator,)+tuple(self.data))

	def __str__(self):
		s = [' [] ' if i==self.elevator else '    '\
				for i in range(NFLOORS)]
		g = zip(ascii_uppercase, ascii_lowercase)
		for i in self.states():
			# For each of the pairs in state i ... do printing
			for _ in range(self.data[i]):
				upper,lower = next(g)
				c = ['--']*NFLOORS
				if microchip(i)==RTG(i):
					c[microchip(i)] = upper+lower
				else:
					c[RTG(i)] = upper+' '
					c[microchip(i)] = lower+' '

				for k,ci in enumerate(c):
					s[k] += " "+ci
		# Print reversed so top floor prints first
		return '\n'.join(reversed(s))

	def states(self):
		# Iterator over states which have at least one item
		for i in range(len(self.data)):
			if self.data[i]:
				yield i

	def valid(self):
		# A state is valid if no microchips are in the presence of an RTG and
		# are not connected to their own RTG.
		#
		# Make a list of locations with lonely chips, and a list of locations
		# with generators. Then check that no location has both

		lonely_chips = [False]*NFLOORS
		generator = [False]*NFLOORS
		for i in self.states():
			if not chip_with_generator(i):
				lonely_chips[microchip(i)] = True
			generator[RTG(i)] = True

		# Valid if on each floor we don't have both a generator and lonely chip
		return not any(lc and g for lc,g in zip(lonely_chips, generator))

	def directions(self):
		if self.elevator>0:
			yield -1
		if self.elevator<NFLOORS-1:
			yield 1

	def factor_items_on_floor(self, floor):
		# Return index for all items on given floor
		# First element of return value is a factor which is used to work out
		# how to change the state when moving the given item.
		for i in self.states():
			if RTG(i)==floor:
				# If we move a generator, state changes by NFLOORS
				yield (NFLOORS, i)
			if microchip(i)==floor:
				# If we move a chip, state changes by 1
				yield (1, i)

	def moves(self, seen):
		# Generator which yields all feasible moves
		# We can move elevator up or down and we can take one or two items.
		#
		# If a generator is moved up or down this alters its state by +-4
		# If a chip is moved up or down its state is altered by +- 1
		for d in self.directions():
			for j in self.move_d(d):
				if j.valid() and j not in seen:
					seen.add(j)
					yield j

	def move_d(self, d, nmoves=2):
		# nmoves=2 indicates we can still move 2 items on current go
		for (factor, index) in self.factor_items_on_floor(self.elevator):
			new = State(self)
			new.data[index] -= 1
			new.data[index+factor*d] += 1
			if nmoves>1:
				yield from new.move_d(d, nmoves-1)
			# Move the elevator and yield
			new.elevator += d
			yield new

def print_set(myset):
	s = "--------------------\n"
	s += "--------------------\n"
	for i in myset:
		s += str(i)+"\n"
		s += "--------------------\n"
	s += "--------------------\n"
	print(s)

def solve(state, winner):
	# Keep a set of seen states
	# And for each number of moves, n, keep a set of states which can be
	# reached in n moves
	#
	# Now we can find states obtainable in n+1 moves using states obtainable in
	# n moves. Excluding states already seen since they can be reached in fewer
	# moves.
	seen = set()
	seen.add(state)

	turn_sets = [set()]
	turn_sets[0].add(state)

	for i in range(1,100):
		print("Calculating move",i)
		turn_sets.append(set())
		for start in turn_sets[-2]:
			for new in start.moves(seen):
				turn_sets[-1].add(new)
				if new == winner:
					print("Found winner in {} steps".format(i))
					return turn_sets

	raise Exception("Did not find the winner in {} steps".format(i))

def reverse_engineer(turn_sets, winner):
	# Search for a path of moves back towards starting position
	turn = len(turn_sets)-2 # Turn number of turn before winner
	yield winner

	while turn>=0:
		for path in winner.moves(set()):
			if path in turn_sets[turn]:
				yield path
				winner = path # Now continue searching back from path
				turn -= 1
				break
		else:
			raise Exception("Could not find any state from previous turn")

def main(state):
	# Construct the winning state given the input state
	# This is with everything on the top floor, including the elevator
	winner = State()
	winner.data[NFLOORS**2-1] = sum(state.data)
	winner.elevator = NFLOORS-1

	print(state)
	print('')
	print(winner)
	turn_sets = solve(state, winner)
	for i,step in enumerate(reversed(list(reverse_engineer(turn_sets, winner)))):
		print(i, "----------")
		print(step)

if __name__=="__main__":
	example = State()
	example.data[4] = 1
	example.data[8] = 1

	given = State()
	given.data[0] = 1
	given.data[6] = 4

	part2 = State()
	part2.data[0] = 3
	part2.data[6] = 4

	# main(example)
	# main(given)
	main(part2)
