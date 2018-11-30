#!/usr/bin/env python3

from copy import deepcopy
from heapq import *

def read(fname):
	d = dict()
	with open(fname, 'r') as f:
		next(f)
		for line in f:
			u = line.split()
			d[u[0]] = Spell(*(int(x) for x in u[1:]))

	return d

def read_boss(fname):
	d = dict()
	with open(fname, 'r') as f:
		for line in f:
			u = line.split(':')
			d[u[0]] = int(u[1])
	return d

class Spell(object):
	def __init__(self, cost_mana, damage, hit_points, armor, mana_bonus, n_turns_effective):
		self.cost_mana = cost_mana
		self.damage = damage
		self.hit_points = hit_points
		self.armor = armor
		self.mana_bonus = mana_bonus
		self.n_turns_effective = n_turns_effective

	def __str__(self):
		return " ".join("{:3d}".format(self.__dict__.get(prop)) for prop in
["cost_mana", "damage", "hit_points", "armor", "mana_bonus", "n_turns_effective"])

class EndGameException(BaseException):
	def __init__(self, mana_spent):
		self.mana_spent = mana_spent

class VictoryException(EndGameException):
	def __str__(self):
		return "Player won"

class LossException(EndGameException):
	def __str__(self):
		return "Player lost"

class State(object):
	def __init__(self, wizard_hp, wizard_mana, boss_hp, boss_damage, part2=False):
		self.wizard_hp = wizard_hp
		self.wizard_mana = wizard_mana
		self.wizard_armor = 0
		self.boss_hp = boss_hp
		self.boss_damage = boss_damage
		self.part2 = part2
		# A dict with strings for keys and spell objects for values
		self.spells = dict()
		self.mana_spent = 0

	def choices(self, spells):
		# Yield possible spells which can be played
		for spell_name in spells.keys():
			if spell_name not in self.spells or (spell_name in self.spells and self.spells[spell_name].n_turns_effective == 1):
				if self.wizard_mana >= spells[spell_name].cost_mana:
					yield spell_name

	def __str__(self):
		s  = "Player has {} hit points, {} armor, {} mana\n".format(
			self.wizard_hp, self.wizard_armor, self.wizard_mana)
		s += "Boss has {} hit points".format(self.boss_hp)
		# for key, spell in self.spells.items():
		# 	s += "{} active. It's timer is {}\n".format(key, spell.n_turns_effective)
		return s

	def check_victory(self):
		assert self.boss_hp > 0 or self.wizard_hp > 0
		if self.boss_hp <= 0:
			raise VictoryException(self.mana_spent)
		if self.wizard_hp <= 0:
			raise LossException(self.mana_spent)

	def turn(self, spell_name, spells):
		# Do a turn without modifying the current state object
		spell = deepcopy(spells[spell_name])
		new = deepcopy(self)
		new.turn_(spell_name, spell)
		return new

	def turn_(self, spell_name, spell):
		# Update state following wizard turn where the given wizard_spell
		# is played, and a turn for the boss. (i.e. two turns are played)
		if self.part2:
			# print("Player loses 1 HP for hard mode")
			self.wizard_hp -= 1
			self.check_victory()

		self.do_spells()
		self.check_victory()

		# Cast a spell
		assert spell_name not in self.spells
		assert self.wizard_mana >= spell.cost_mana
		# print("Player casts {}".format(spell_name))

		self.wizard_mana -= spell.cost_mana
		self.mana_spent += spell.cost_mana
		if spell.n_turns_effective > 1:
			self.spells[spell_name] = spell
		else:
			self.boss_hp -= spell.damage
			self.wizard_hp += spell.hit_points
		self.check_victory()

		# print("\n-- Boss turn --")
		# print(self)

		self.do_spells()
		self.check_victory()

		# Boss attack
		self.wizard_hp -= max(1, self.boss_damage-self.wizard_armor)
		self.check_victory()

		# print("\n-- Player turn --")
		# print(self)

	def do_spells(self):
		self.wizard_armor = 0
		# Activate the spells
		to_delete = []
		for spell_name, spell in self.spells.items():
			self.boss_hp -= spell.damage
			self.wizard_hp += spell.hit_points
			if spell.armor!=0:
				self.wizard_armor = spell.armor
			self.wizard_mana += spell.mana_bonus
			spell.n_turns_effective -= 1

			# print("{} active; it's timer is now {}.".format(spell_name, spell.n_turns_effective))

			if spell.n_turns_effective == 0:
				to_delete.append(spell_name)
		for spell_name in to_delete:
			del self.spells[spell_name]

def dijkstra(spells, s):
	# Given the available spells and an initial state s,
	# find the path to victory which requires the least total mana usage,

	# The heap contains tuples of the form (mana_spent, state)
	uu = 0
	heap = [(0, uu, s)]
	best = None

	while heap:
		expenditure, _, state = heappop(heap)

		if best is not None and expenditure >= best:
			return best

		for spell in state.choices(spells):
			try:
				new_s = state.turn(spell, spells)
				if best is None or new_s.mana_spent < best:
					uu += 1
					heappush(heap, (new_s.mana_spent, uu, new_s))

			except VictoryException as e:
				if best is None or e.mana_spent < best:
					best = e.mana_spent

			except LossException:
				pass

if __name__=="__main__":
	import sys
	spells = read(sys.argv[1])

	for spell in spells:
		print("{:12s} {}".format(spell, str(spells[spell])))

	boss = read_boss(sys.argv[2])

	# Part 1
	s = State(50, 500, boss["Hit Points"], boss["Damage"])
	op = dijkstra(spells, s)
	print("Part 1:", op)

	# Part 2
	s = State(50, 500, boss["Hit Points"], boss["Damage"], part2=True)
	op = dijkstra(spells, s)
	print("Part 2:", op)

	# # Test 1
	# s = State(10, 250, 13, 8)
	# print(s)
	# for spell in ["Poison", "MagicMissile"]:
	# 	try:
	# 		print(list(s.choices(spells)))
	# 		s = s.turn(spell, spells)
	# 	except EndGameException as e:
	# 		print(e)
	# 		print("Expenditure = {}".format(e.mana_spent))
	# 		break

	# print("--------------------")

	# # Test 2
	# s = State(10, 250, 14, 8)
	# print(s)
	# for spell in ["Recharge", "Shield", "Drain", "Poison", "MagicMissile"]:
	# 	try:
	# 		print(list(s.choices(spells)))
	# 		s = s.turn(spell, spells)
	# 	except EndGameException as e:
	# 		print(e)
	# 		print("Expenditure = {}".format(e.mana_spent))
	# 		break

	# print("--------------------")
	# # Test 3
	# s = State(100, 1000, 1400, 8)
	# print(s)
	# for spell in ["Poison", "Shield", "MagicMissile", "Poison"]:
	# 	try:
	# 		print(list(s.choices(spells)))
	# 		s = s.turn(spell, spells)
	# 	except EndGameException as e:
	# 		print(e)
	# 		print("Expenditure = {}".format(e.mana_spent))
	# 		break
