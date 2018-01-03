#!/usr/bin/env python3

q = input()

# Part 1
s = sum(int(q[i]) for i in range(len(q)) if q[i] == q[(i+1)%len(q)])

print("Part 1: {}".format(s))

# Part 2
s = sum(int(q[i]) for i in range(len(q)) if q[i] == q[(i+len(q)//2)%len(q)])
print("Part 2: {}".format(s))
