#!/usr/bin/env python3

def generator(start, factor):
    x = start
    while True:
        x *= factor
        x %= 2147483647
        yield x

def part1(Astart, Bstart, n):
    gA = generator(Astart, 16807)
    gB = generator(Bstart, 48271)

    return count_matching(gA, gB, n)

def part2(Astart, Bstart, n):
    gA = filter(lambda x: not x&3, generator(Astart, 16807))
    gB = filter(lambda x: not x&7, generator(Bstart, 48271))

    return count_matching(gA, gB, n)

def count_matching(gA, gB, n):

    # For checking last 16 bits
    u = (1 << 16) - 1

    return sum(1 for a, b, _ in zip(gA, gB, range(n)) if a&u == b&u)

if __name__=="__main__":

    Aexample = 65
    Bexample = 8921

    Ainput = 699
    Binput = 124

    # Example 1
    # print(part1(Aexample, Bexample, int(4e7)))

    # Part 1
    print(part1(Ainput, Binput, int(4e7)))

    # Example 2
    # print(part2(Aexample, Bexample, int(5e6)))

    # Part 2
    print(part2(Ainput, Binput, int(5e6)))
