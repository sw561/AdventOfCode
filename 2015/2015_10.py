#!/usr/bin/env python3

def runs(s):
	count = 1
	i_prev = s[0]
	for i in s[1:]:
		if i == i_prev:
			count += 1
		else:
			yield count, i_prev
			count = 1
			i_prev = i
	yield count, i_prev

def f(x):
	return "".join("{}{}".format(*x) for x in runs(x))

if __name__=="__main__":

	# Test cases
	# print("1", f("1"))
	# print("11", f("11"))
	# print("21", f("21"))
	# print("1211", f("1211"))
	# print("111221", f("111221"))

	x = input()
	for i in range(40):
		x = f(x)
	print("Part 1:", len(x))

	for i in range(10):
		x = f(x)
	print("Part 2:", len(x))
