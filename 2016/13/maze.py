#!/usr/bin/env python3

NUMBER = 10

def wall(pos):
	(y, x) = pos
	s = x*(x+3+2*y) + y*(y+1) + NUMBER
	s = sum(1 for i in bin(s) if i=='1')
	return s%2

def print_map(route=None, n=10):
	print('   '+''.join(str(i%10) for i in range(n)))
	def char(pos):
		if wall(pos): return '#'
		elif route is not None and pos in route: return 'O'
		else: return '.'
	for row in range(n):
		prefix = '{:2} '.format(row)
		print(prefix+''.join(char((row, col)) for col in range(n)))

def candidate_moves(pos):
	(y, x) = pos
	yield (y+1, x)
	if y>0:
		yield (y-1, x)
	yield (y, x+1)
	if x>0:
		yield (y, x-1)

def moves(pos, seen):
	for new_pos in candidate_moves(pos):
		if not wall(new_pos) and new_pos not in seen:
			seen.add(new_pos)
			yield new_pos

def dijkstra(winner, maxturns=1000):
	pos = (1,1)
	seen = set()
	seen.add(pos)

	turn_sets = [set()]
	turn_sets[0].add(pos)

	for i in range(1, maxturns):
		turn_sets.append(set())
		for start in turn_sets[-2]:
			for new_pos in moves(start, seen):
				turn_sets[-1].add(new_pos)
				if new_pos==winner:
					print("Found it in {} steps".format(i))
					return turn_sets
		if i==50:
			print("Total number of places in {} steps is {}".format(i, len(seen)))
	raise Exception("No route found on step {}".format(i))

def reverse_engineer(turn_sets, winner):
	turn = len(turn_sets)-2
	yield winner

	while turn>=0:
		for step in moves(winner, set()):
			if step in turn_sets[turn]:
				yield step
				winner = step
				turn -= 1
				break
		else:
			raise Exception("Could not reverse engineer")

# Indices are swapped round because the problem is presented in terms of (x,y)
# coordinates, but I prefer to think of it as a matrix which is normally
# accessed as M[row][col] i.e. M[y][x]

# example
NUMBER = 10
winner = (4,7)
turn_sets = dijkstra(winner)
route = set(reverse_engineer(turn_sets, winner))
print_map(route=route)

# Problem
NUMBER = 1358
winner = (39, 31)
turn_sets = dijkstra(winner)
route = set(reverse_engineer(turn_sets, winner))
print_map(route=route, n=45)
