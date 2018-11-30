#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def vowels(s, n):
	count_vowels = 0
	for i in s:
		if i in "aeiou":
			count_vowels += 1
		if count_vowels >= n:
			return True
	return False

def double_letter(s):
	return any(i==j for i, j in zip(s, s[1:]))

bad_strings = ["ab", "cd", "pq", "xy"]
def has_bad_strings(s):
	return any(s[i:i+2] in bad_strings for i in range(len(s)-1))

def nice(s):
	return vowels(s, 3) and double_letter(s) and not has_bad_strings(s)

def twice_appearing_pair(s):
	d = set()
	for i in range(2, len(s)-1):
		# Want to avoid overlapping pairs!
		d.add(s[i-2:i])
		if s[i:i+2] in d:
			return True
	return False

def repeated_letter_with_space(s):
	return any(i==j for i, j in zip(s, s[2:]))

def very_nice(s):
	return twice_appearing_pair(s) and repeated_letter_with_space(s)

def read(fname):
	with open(fname, 'r') as f:
		data = f.read().split()
	return data

if __name__=="__main__":
	import sys

	data = read(sys.argv[1])

	# Count nice strings
	print(sum(1 for s in data if nice(s)))

	# Part 2
	print(sum(1 for s in data if very_nice(s)))
