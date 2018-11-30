#!/usr/bin/env python3

import hashlib

def mine(x, nzeros=5):
	h = hashlib.md5()
	h.update(x)
	u = 1
	while True:
		hnew = h.copy()
		hnew.update(bytearray(str(u), encoding="utf-8"))

		if all(digit=="0" for digit in hnew.hexdigest()[:nzeros]):
			print("u:", u)
			print("hnew.hexdigest():", hnew.hexdigest())
			break

		u += 1

# mine(b"abcdef")
# mine(b"pqrstuv")

# Part 1
mine(b"bgvyzdsv")

# Part 2
mine(b"bgvyzdsv", nzeros=6)
