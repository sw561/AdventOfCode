#!/usr/bin/env python3

from itertools import chain
import numpy as np

actions = dict()
def action(f):
    actions[f.__name__] = f

@action
def s(u, d, i, x):
    i = (i-int(x))%len(u)
    return i

@action
def x(s, d, i, a, b):
    a, b = ((int(x)+i)%len(s) for x in (a, b))
    s[a], s[b] = s[b], s[a]
    d[s[a]], d[s[b]] = a, b
    return i

@action
def p(s, d, i, a, b):
    ai = d[a]
    bi = d[b]
    s[ai], s[bi] = s[bi], s[ai]
    d[a], d[b] = bi, ai
    return i

def p(u, i):
    print("".join(str(x) for x in chain(u[i:], u[:i])))

def main(fname, n, repeat=1):
    with open(fname, 'r') as f:
        l = next(f)
    commands = l.strip().split(',')

    u = [chr(x) for x in range(97, 97+n)]
    d = dict(((x, i) for i, x in enumerate(u)))
    i = 0
    # print(u)
    # print(d)

    for _ in range(repeat):
        for c in commands:
            # Do something
            i = actions[c[0]](u, d, i, *c[1:].split('/'))

            # print(u, i)
            # print(", ".join("{}: {}".format(key, d[key]) for key in sorted(d.keys())))

    return u, i

if __name__=="__main__":
    import sys

    u, i = main(sys.argv[1], int(sys.argv[2]))

    # Part 1
    p(u, i)

    # Part 2
    u, i = main(sys.argv[1], int(sys.argv[2]), repeat=1000)
    p(u, i)
