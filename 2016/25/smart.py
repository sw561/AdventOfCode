#!/usr/bin/env python3

# Python fast version of the assembunny program

import func_bunny
import sys

def f(a):
	d = 182 * 14 + a

	while True:
		a = d
		while a:
			yield a%2
			a //= 2

def test_smart(a):
	fname = "input"
	func_bunny.code = [line.strip().split() for line in open(fname, 'r')]

	for i, (x, y) in enumerate(zip(f(a), func_bunny.run(a))):
		assert x==y
		if i==50:
			return

def test():
	for a in range(0, 40):
		test_smart(a)

	print("Test successful")

# test()

# Code output is 0, 1, 0, 1, 0
#
# which means when we divide d by 2 we get even, odd, even, odd, even, etc
#
# implies written in binary the number is 1010101...
# 1, 2, 5, 10, 21, 42, ...

print("182*14:", 182*14)

i = 1
while i < 182 * 14:
	if i%2:
		i *= 2
	else:
		i *= 2
		i += 1
	print(i)

a = i-182*14
print("initial a is", a)

for i, x in enumerate(f(a)):
	print(x)
	if i==40:
		break
