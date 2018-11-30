#!/usr/bin/env python3

import hashlib

# In a grid of size 4x4.
# Need to move from (0,0) to (3,3)
#
# On each move, we can go U, D, L or R depending on the md5 of passcode + path
# U by md5_hash[0]
# D by md5_hash[1]
# L by md5_hash[2]
# R by md5_hash[3]
#
# If the character in the hash is in [b,c,d,e,f] then the door is open

def mymd5(s, i):
	# Do hashes of leading + index where index is an integer.
	m = hashlib.md5()
	m.update((s+i).encode('utf-8'))
	return m.hexdigest()

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

unlocked_hash_chars = ['b','c','d','e','f']

def possible_destinations(passcode, path, pos):
	(x, y) = pos
	h = mymd5(passcode, path)
	# print("Hash of",PASSCODE,path,h)
	if x>0 and h[LEFT] in unlocked_hash_chars:
		yield ('L', (x-1, y))
	if x<3 and h[RIGHT] in unlocked_hash_chars:
		yield ('R', (x+1, y))
	if y>0 and h[DOWN] in unlocked_hash_chars:
		yield ('D', (x, y-1))
	if y<3 and h[UP] in unlocked_hash_chars:
		yield ('U', (x, y+1))

def dijkstra(passcode):
	pos=(0,3)

	# turn_dict is a dict of form path -> position
	turn_dict = dict()
	turn_dict[''] = pos

	shortest_path = None
	longest_path = None
	while turn_dict:
		turn_dict_old = turn_dict
		turn_dict = dict()
		for path, pos in turn_dict_old.items():
			for direction, new_pos in possible_destinations(passcode, path, pos):
				if new_pos==(3,0):
					# return path+direction for finding shortest_path only
					if shortest_path is None:
						shortest_path = path+direction
					longest_path = path+direction
				else:
					turn_dict[path+direction] = new_pos

		# from pprint import pprint
		# pprint(turn_dict)
	return (shortest_path, longest_path)

def main(passcode):
	shortest, longest = dijkstra(passcode)
	if longest is not None:
		print(shortest, len(longest))
	else:
		print(shortest)

# Examples
main("hijkl")
main("ihgpwlah")
main("kglvqrro")
main("ulqzkmiv")

# Part 1
main("veumntbg")
