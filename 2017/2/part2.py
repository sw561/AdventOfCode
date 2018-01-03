#!/usr/bin/env python3

import sys

def find_divisible(x):

    for i in range(len(x)):
        a = x[i]
        for b in x[i+1:]:
            if not a%b:
                return a//b
            if not b%a:
                return b//a

total = 0
for line in open(sys.argv[1], 'r'):
    s = list(int(x) for x in line.split())
    total += find_divisible(s)

print("total:", total)
