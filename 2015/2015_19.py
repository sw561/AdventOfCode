#!/usr/bin/env python3

def separate(x):
	# Separate string into a list of substrings each of which starts with a
	# capital letter

	def get_capital_indices(x):
		for i in range(len(x)):
			if ord('A') <= ord(x[i]) <= ord('Z'):
				yield i

	def adjacent_pairs(x, n):
		prev = next(x)
		for i in x:
			yield prev, i
			prev = i
		yield prev, n

	return [x[s:e] for s, e in adjacent_pairs(get_capital_indices(x), len(x))]

def read(fname):
	replacements = dict()
	s = None
	with open(fname, 'r') as f:
		for line in f:
			if "=" in line:
				line = line.replace('>', '')
				x, y = (u.strip() for u in line.split('='))
				if x not in replacements:
					replacements[x] = []
				replacements[x].append(y)

			elif line:
				s = line.strip()

	return replacements, s

def insert(s, i, j):
	# Insert j at position i. Just yield everything in the right order
	yield from s[:i]
	yield j
	yield from s[i+1:]

def use_replacements(s, replacements):
	for i in range(len(s)):
		if s[i] in replacements:
			for j in replacements[s[i]]:
				yield "".join(insert(s, i, j))

if __name__=="__main__":
	import sys
	replacements, s = read(sys.argv[1])

	if s is None:
		s = sys.argv[2]

	s = separate(s)

	# for r in replacements:
	# 	print("{}: {}".format(r, replacements[r]))
	# print("s:", s)

	print("Part 1:", len(set((use_replacements(s, replacements)))))

	# For part 2, count the number of tokens that are Rn, Y and Ar
	cRnAr = 0
	cY = 0
	for i in s:
		if i in ["Rn", "Ar"]:
			cRnAr += 1
		elif i == "Y":
			cY += 1

	print("Part 2:", len(s) - cRnAr - 2*cY - 1)
