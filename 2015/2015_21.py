#!/usr/bin/env python3

from math import ceil
from itertools import combinations, product

def read(fname):
	d = dict()
	with open(fname, 'r') as f:
		for line in f:
			u = line.split()
			if not u: continue
			v = u[0]
			if v[-1] == ':':
				key = v[:-1]
				d[key] = dict()
			else:
				if len(u) > 4:
					name = " ".join(u[:2])
				else:
					name = u[0]
				d[key][name] = tuple(int(x) for x in u[-3:])

	return d

def read_boss(fname):
	d = dict()
	with open(fname, 'r') as f:
		for line in f:
			u = line.split(':')
			d[u[0]] = int(u[1])
	return d

def build_character(options, choice):
	cost = 0
	char = dict()
	char["Hit Points"] = 100
	char["Damage"] = 0
	char["Armor"] = 0
	def add_item(c, d, a):
		nonlocal cost
		cost += c
		char["Damage"] += d
		char["Armor"] += a

	add_item(*options["Weapons"][choice[0]])

	for armor in choice[1]:
		add_item(*options["Armor"][armor])

	for ring in choice[2]:
		add_item(*options["Rings"][ring])

	return cost, char

def battle(character, enemy):
	# Return true if character wins, false otherwise
	ch_attack = character["Damage"] - enemy["Armor"]
	en_attack = enemy["Damage"] - character["Armor"]

	ch_turns_to_kill = int(ceil(enemy["Hit Points"] / max(1, ch_attack)))
	en_turns_to_kill = int(ceil(character["Hit Points"] / max(1, en_attack)))

	return ch_turns_to_kill <= en_turns_to_kill

def combinations_up_to_n(iterable, r):
	# Yield all combinations with length <= r
	for i in range(0, r+1):
		yield from combinations(iterable, i)

def gen_choices(options):
	yield from product(options["Weapons"].keys(),
		combinations_up_to_n(options["Armor"].keys(), 1),
		combinations_up_to_n(options["Rings"].keys(), 2),
		)

if __name__=="__main__":
	# # Test case
	# character = {"Hit Points":  8, "Damage": 5, "Armor": 5}
	# boss      = {"Hit Points": 12, "Damage": 7, "Armor": 2}
	# print(battle(character, boss))

	import sys
	options = read(sys.argv[1])

	# for key in options:
	# 	print(key)
	# 	for q in options[key]:
	# 		print("    ", q, options[key][q])

	enemy = read_boss(sys.argv[2])
	print(enemy)

	# for i in gen_choices(options):
	# 	print(i, *build_character(options, i))

	# Part 1
	def key_f(choice):
		cost, character = build_character(options, choice)
		if battle(character, enemy):
			return cost
		else:
			return 1000000
	choice = min(gen_choices(options), key=key_f)
	cost, character = build_character(options, choice)
	print("Part 1:")
	print("choice:", choice)
	print("cost, character:", cost, character)
	print("battle(character, enemy):", battle(character, enemy))

	def key_f(choice):
		cost, character = build_character(options, choice)
		if battle(character, enemy):
			return -1
		else:
			return cost
	choice = max(gen_choices(options), key=key_f)
	cost, character = build_character(options, choice)
	print("Part 2:")
	print("choice:", choice)
	print("cost, character:", cost, character)
	print("battle(character, enemy):", battle(character, enemy))
