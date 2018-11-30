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

class Chemical(object):
	def __init__(self, s):
		# Initialise using a string
		if type(s) is str:
			self.data = separate(s)
		else:
			self.data = s

	@classmethod
	def insert(cls, chemical, i, x, k):
		# Insert x into the chemical at given indices
		if type(x) is str:
			x = Chemical(x)

		data = chemical.data[:i] + x.data + chemical[k:]
		return cls(data)

	def __str__(self):
		return "".join(self.data)

	def __hash__(self):
		return hash(str(self))

	def __eq__(self, other):
		return str(self) == str(other)

	def __len__(self):
		return len(self.data)

	def __getitem__(self, i):
		return self.data[i]

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

def use_replacements(s, replacements):
	for i in range(len(s)):
		if s[i] in replacements:
			for x in replacements[s[i]]:
				yield Chemical.insert(s, i, x, i+1)

def invert(replacements):
	# Make a new dictionary which gives me left hand side of replacement
	# operations for a given string.
	#
	# Also return longest right hand side object which we need to consider
	inv_replacements = dict()
	for key in replacements:
		if key=="e": continue
		for u in replacements[key]:
			if u not in inv_replacements:
				inv_replacements[u] = key
			else:
				raise Exception("Multiple possibilities!")

	return inv_replacements

def use_inv_replacements(s, inv_replacements, longest):
	# Need to loop over all possible objects
	for i in range(len(s)):
		for j in range(1, longest+1):
			if j > len(s):
				break
			t = str(Chemical(s[i:i+j]))
			if t in inv_replacements:
				yield Chemical.insert(s, i, inv_replacements[t], i+j)

def all_inv_replacements(inv_replacements, longest, current, seen):
	for s in current:
		for x in use_inv_replacements(s, inv_replacements, longest):
			if x not in seen:
				yield x

def bfs(s, inv_replacements, longest, targets):
	# Use breadth first search to find minimum number of steps to create s

	step = 0
	seen = {s}
	current = {s}
	while step < 6:
		step += 1
		n = set(all_inv_replacements(inv_replacements, longest, current, seen))
		# print("step, {} n:\n{}".format(step, "\n".join(str(x) for x in n)))
		current = n
		seen |= current
		# print("seen:")
		# print(" ".join(sorted((str(x) for x in seen), key=lambda x: (len(x), x))))
		print("step, len(seen), len(current):", step, len(seen), len(current))
		if any(target in current for target in targets):
			return step + 1

if __name__=="__main__":
	import sys
	replacements, s = read(sys.argv[1])

	if s is None:
		s = sys.argv[2]

	s = Chemical(s)

	# print("replacements:", replacements)
	# for r in replacements:
	# 	print("{}: {}".format(r, replacements[r]))
	# print("s:", s)
	print("Part 1:", len(set(use_replacements(s, replacements))))

	inv_replacements = invert(replacements)
	targets = replacements["e"]
	# print("inv_replacements:", inv_replacements)
	# for r in inv_replacements:
	# 	print("{}: {}".format(r, inv_replacements[r]))

	longest = max(len(x) for x in inv_replacements.keys())
	print("longest:", longest)
	print("targets:", targets)

	# for x in use_inv_replacements(s, inv_replacements, longest):
	# 	print(x)

	step = bfs(s, inv_replacements, longest, targets)
	print("step:", step)
