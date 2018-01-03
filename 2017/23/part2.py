#!/usr/bin/env python3

from math import sqrt

def isprime(x):
    return all(x%b for b in range(2, int(sqrt(x))+1))

b = 100*65 + 100000
c = b + 17000
# print("b, c:", b, c)

h = sum(1 for x in range(b, c+1, 17) if not isprime(x))
print(h)
