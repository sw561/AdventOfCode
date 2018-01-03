#!/usr/bin/env python3

from itertools import chain
import numpy as np

def construct_matrix(s):
    # Given a string which is a permutation of x = "abcde..."
    # construct a matrix s.t. P x = s

    p = np.zeros((len(s), len(s)), dtype=int)

    for i, x in enumerate(s):
        p[i, ord(x)-ord('a')] = 1

    return p

def perm(fname, n):
    p = [chr(ord('a')+x) for x in range(n)]
    i = 0
    with open(fname, 'r') as f:
        for line_ in f:
            for line in line_.strip().split(','):
                if line[0]=="s":
                    i = (i-int(line[1:])) % n
                elif line[0]=="x":
                    a, b = (int(x) for x in line[1:].split('/'))

                    a = (a+i)%n
                    b = (b+i)%n
                    p[a], p[b] = p[b], p[a]

    s = "".join(u for u in chain(p[i:], p[:i]))
    print("s:", s)
    return construct_matrix(s)

def reversed_label_switching(fname, n):
    # Get the label switching commands, in reverse order!

    p = [chr(ord('a')+x) for x in range(n)]
    with open(fname, 'r') as f:
        for line_ in f:
            for line in reversed(line_.strip().split(',')):
                if line[0]=="p":
                    a, b = (ord(x)-ord('a') for x in line[1:].split('/'))

                    p[a], p[b] = p[b], p[a]

    s = "".join(p)
    print("s:", s)
    return construct_matrix(s)

def matrix_pow(A, n):
    # Raise a matrix, A, to the power n.
    if n == 1:
        return A

    u = matrix_pow(A, n//2)
    B = np.dot(u, u)
    if n%2:
        B = np.dot(B, A)
    return B

if __name__=="__main__":
    import sys

    p = perm(sys.argv[1], int(sys.argv[2]))
    d = reversed_label_switching(sys.argv[1], int(sys.argv[2]))

    # print("p:\n", p)
    # print("d:\n", d)

    # Part 1, apply P once
    print("Part 1")
    x = np.fromiter(range(int(sys.argv[2])), dtype=int)
    y = np.dot(p, np.dot(d, x))
    print("".join(chr(ord('a') + x) for x in y))

    print("Part 2")
    p = matrix_pow(p, int(1e9))
    d = matrix_pow(d, int(1e9))
    # print("p:\n", p)
    # print("d:\n", d)
    y = np.dot(p, np.dot(d, x))
    print("".join(chr(ord('a') + x) for x in y))
