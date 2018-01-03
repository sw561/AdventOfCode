#!/usr/bin/env python3

from functools import reduce

def solve(u, n, repeat=1):
    i = 0
    L = list(range(n))
    skip_length = 0

    for _ in range(repeat):
        for ui in u:
            for j, k in zip(range(i, i+ui//2), reversed(range(i, i+ui))):
                j %= n
                k %= n
                L[j], L[k] = L[k], L[j]

            i = (i + ui + skip_length)%n
            skip_length += 1

            # print("ui:", ui)
            # print(" ".join(str(x) for x in L))
            # print(i)
            # print("--------------------")

    return L[0] * L[1], L

def part1(fname, n):
    with open(fname, 'r') as f:
        u = [int(x) for x in next(f).split(',')]
    prod, _ = solve(u, n)
    return prod

def part2(fname, n):
    with open(fname, 'r') as f:
        u = [ord(x) for x in next(f).strip()]

    u.extend([17, 31, 73, 47, 23])

    _, L = solve(u, n, repeat=64)

    return "".join("{:02x}".format(x) for x in dense(L))

def dense(L):
    for i in range(0, 256, 16):
        yield reduce(lambda x, y: x^y, L[i:i+16])

if __name__=="__main__":

    # Part 1
    print("part1('example', 5): {:4d}".format(part1('example', 5)))
    print("part1('input', 256): {:4d}".format(part1('input', 256)))

    # Part 2
    print("part2('example2', 256):", part2('example2', 256))
    print("part2('input', 256):", part2('input', 256))
