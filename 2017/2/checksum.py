#!/usr/bin/env python3

import sys

def min_max(u):
    l = next(u)
    t = l
    for i in u:
        if i<l:
            l = i
        if i>t:
            t = i
    return l, t

total = 0
for line in open(sys.argv[1], 'r'):
    l, t = min_max(int(x) for x in line.split())
    total += t - l

print("total:", total)
