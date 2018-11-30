#!/usr/bin/env python3

from itertools import combinations_with_replacement
import numpy as np

def read(fname):
	data = []
	with open(fname, 'r') as f:
		for line in f:
			_, props = line.split(':')

			props = [int(x.split()[1]) for x in props.split(',')]
			data.append(props)

	return np.transpose(np.array(data))

def gen_recipe(total, n_ingredients):
	recipe = np.zeros(n_ingredients, dtype=int)
	for c in combinations_with_replacement(range(total+1), n_ingredients-1):
		total_so_far = 0
		for i, ci in enumerate(c):
			recipe[i] = ci-total_so_far
			total_so_far += recipe[i]
		recipe[-1] = total - total_so_far
		yield recipe

def gen_recipe2(total, n_ingredients, m_calories):

	# To get values for final two ingredients we can solve the linear system,
	# consisting of two equations:
	# Firstly all ingredients sum to 100
	# Secondly the total calories is 500
	#
	# m_calories is the final row of the matrix: m_calories . ingredients = calories

	matrix = np.array([[1, 1], m_calories[-2:]])
	m_inv = np.linalg.inv(matrix)

	b = np.zeros(2, dtype=int)

	recipe = np.zeros(n_ingredients, dtype=int)

	for c in combinations_with_replacement(range(total+1), n_ingredients-2):
		total_so_far = 0
		calories_so_far = 0
		for i, ci in enumerate(c):
			recipe[i] = ci-total_so_far
			total_so_far += recipe[i]
			calories_so_far += m_calories[i] * recipe[i]

		b[0] = 100 - total_so_far
		b[1] = 500 - calories_so_far

		x = np.dot(m_inv, b)

		# Check each element of xi is an integer >= 0
		if all(xi > -1e-5 and abs(round(xi)-xi) < 1e-5 for xi in x):
			recipe[-2] = round(x[0])
			recipe[-1] = round(x[1])
			yield recipe

def score(m, x):
	t = 1
	for i in np.dot(m, x):
		if i <= 0: return 0
		t *= i
	return t

if __name__=="__main__":
	import sys
	m = read(sys.argv[1])
	# print("m:", m)

	m_score = m[:-1] # don't need calories when calculating score

	# Part 1
	maxi = max(score(m_score, x) for x in gen_recipe(100, len(m[0])))
	print("Part 1:", maxi)

	# Part 2
	maxi = max(score(m_score, x) for x in gen_recipe2(100, len(m[0]), m[-1]))
	print("Part 2:", maxi)
