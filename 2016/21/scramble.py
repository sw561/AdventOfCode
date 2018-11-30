#!/usr/bin/env python3

def get_input():
	while True:
		try:
			x = input()
		except EOFError:
			return
		yield x

def swap_positions(i, j, password):
	password[i], password[j] = password[j], password[i]
	return password

def swap_letters(a, b, password):
	i = password.index(a)
	j = password.index(b)
	swap_positions(i, j, password)
	return password

def reverse(x, y, password):
	password = password[:x] + password[x:y+1][::-1] + password[y+1:]
	return password

def rotate_left(i, password):
	password = password[i:] + password[:i]
	return password

def rotate_right(i, password):
	return rotate_left(len(password)-i, password)

def rotate_based(q, password):
	i = password.index(q)
	if i>=4:
		increment = 1
	else:
		increment = 0
	index = 1 + i + increment
	# print("Rotating by",index)
	return rotate_right(index, password)

def move(x, y, password):
	q = password.pop(x)
	password.insert(y, q)
	return password

def reverse_engineer_rotate(x, q, password):
	current = password[:]
	parsed = parse(x)
	print(current)
	for i in range(len(password)):
		candidate = rotate_right(i,password)
		print(i, candidate, parsed(candidate))
		if parsed(candidate)[0] == current[0]:
			return candidate
	exit('YYYYYYY')

def parse(x):
	x = x.split()
	if x[0]=='swap':
		if x[1]=='position':
			return lambda p: swap_positions(int(x[2]), int(x[5]), p)
		elif x[1]=='letter':
			return lambda p: swap_letters(x[2], x[5], p)

	elif x[0]=='reverse':
		return lambda p: reverse(int(x[2]), int(x[4]), p)

	elif x[0]=='rotate':
		if x[1]=='left':
			return lambda p: rotate_left(int(x[2]), p)
		elif x[1]=='right':
			return lambda p: rotate_right(int(x[2]), p)
		elif x[1]=='based':
			return lambda p: rotate_based(x[-1], p)

	elif x[0]=='move':
		return lambda p: move(int(x[2]), int(x[5]), p)

def parse_reverse(xjoined):
	x = xjoined.split()
	# The same in reverse
	if x[0]=='swap' or x[0]=='reverse':
		return parse(xjoined)

	elif x[0]=='rotate':
		if x[1]=='left':
			return lambda p: rotate_right(int(x[2]), p)
		elif x[1]=='right':
			return lambda p: rotate_left(int(x[2]), p)
		elif x[1]=='based':
			# Need to find the rotation index such that when we apply x we
			# recover the current password
			return lambda p: reverse_engineer_rotate(xjoined, x[-1], p)

	elif x[0]=='move':
		return lambda p: move(int(x[5]), int(x[2]), p)

def scramble(password):
	for x in get_input():
		password = parse(x)(password)
		print(x)
		print("".join(password))

def unscramble(password):
	for x in reversed(list(get_input())):
		password = parse_reverse(x)(password)
		print(x)
		print("".join(password))

# Sample
# scramble(list('abcde'))

# For running with input
# scramble(list('abcdefgh'))

# Part 2 - Unscrambling
# Sample does not work since the rules rely on 8 letter password
# unscramble(list('decab'))

# Part 2 with puzzle input
# unscramble(list('fbgdceah'))

# Testing solution to part 2
scramble(list('fhgcdaeb'))
