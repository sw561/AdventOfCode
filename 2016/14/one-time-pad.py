#!/usr/bin/env python3

import hashlib

def mymd5(s, i):
	# Do hashes of leading + index where index is an integer.
	m = hashlib.md5()
	m.update((s+str(i)).encode('utf-8'))
	return m.hexdigest()

def md5(x):
	m = hashlib.md5()
	m.update(x.encode('utf-8'))
	return m.hexdigest()

def stretched_md5(s, i):
	m = hashlib.md5()
	m.update((s+str(i)).encode('utf-8'))
	x = m.hexdigest()
	for _ in range(2016):
		x = md5(x)
	return x

def contains_triple(x):
	# Look for three of the same character in a row
	for j in range(2, len(x)):
		if x[j]==x[j-1]:
			if x[j-1]==x[j-2]:
				return x[j]
	return None

def contains_five(x, i):
	return i*5 in x

def hex_char(x):
	return hex(x)[2] # [2] because hex number starts with 0x

def index_hex(x):
	return int(x, 16)

def key_gen(salt, myhash=mymd5):
	i = 0
	keys_found = 0
	keys = []
	searching = [[] for _ in range(16)]
	i_last = 0

	# Need to search a thousand extra to make sure no reordering has spooked us
	while keys_found<64 or i<i_last+1000:
		# Clean out old searches
		for q in searching:
			while q and q[0]<i:
				# print("Given up on searching for {}".format(q[0]-1000))
				q.pop(0)

		x = myhash(salt, i)

		# See if this satisfies any ongoing searches
		for j in range(16):
			if searching[j] and contains_five(x, hex_char(j)):
				for k in searching[j]:
					keys_found += 1
					keys.append(k-1000)
					print("Found {}th key {}".format(keys_found, k-1000))
					if keys_found==64:
						i_last = i
				searching[j] = []

		# Start new searches
		t = contains_triple(x)
		if t is not None:
			searching[index_hex(t)].append(i+1000)

		i += 1
		if not i%1000:
			print("Making some progress... i={}".format(i))

	s = sorted(keys)
	print(s)
	print('64th element:', s[63])

key_gen('abc')
# key_gen('abc', myhash=stretched_md5)
puzzle_salt = 'qzyelonm'
key_gen(puzzle_salt)
key_gen(puzzle_salt, myhash=stretched_md5)
