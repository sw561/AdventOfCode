#!/usr/bin/env python3

def read(fname):
	data = []
	with open(fname, 'r') as f:
		for line in f:
			yield line.strip()

def count_difference(s):
	d = 2
	i = 1
	while i<len(s)-1:
		if s[i] == "\\":
			if s[i+1] == "x":
				d += 3
				i += 3
			elif s[i+1] in ["\\", "\""]:
				d += 1
				i += 1
		i += 1
	return d

def n_extra(s):
	return 2 + sum(1 for i in s if i in ["\"", "\\"])

if __name__=="__main__":
	import sys

	for i, f in enumerate([count_difference, n_extra], 1):
		print("Part {}: {}".format(i, sum(f(x) for x in read(sys.argv[1]))))
