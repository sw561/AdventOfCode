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

    return L

def dense(L):
    for i in range(0, 256, 16):
        yield reduce(lambda x, y: x^y, L[i:i+16])

def knot_hash(s):
    u = [ord(x) for x in s]
    u.extend([17, 31, 73, 47, 23])

    sparse = solve(u, 256, repeat=64)

    return "".join("{:08b}".format(x) for x in dense(sparse))

def row(s, r):
    s = "{}-{}".format(s, r)
    return knot_hash(s)

def neighbours(grid, pos):
    # Find all neighbours which contain data, not including diagonals

    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        p = pos[0] + dx, pos[1] + dy
        if 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0]):
            if grid[p[0]][p[1]] == '1':
                yield p

def find_tree(grid, pos):
    nodes = set([pos])
    nodes_to_add = [pos] # Stack of nodes to add

    while nodes_to_add:
        pos = nodes_to_add.pop()

        for ci in neighbours(grid, pos):
            if ci not in nodes:
                nodes_to_add.append(ci)
                nodes.add(ci)

    return nodes

def find_all_groups(grid):
    visited = set()
    for i in range(128):
        for j in range(128):
            if (i, j) in visited or grid[i][j]=='0':
                continue
            group = find_tree(grid, (i, j))
            yield group
            visited.update(group)

def main(s):
    rows = [row(s, r) for r in range(128)]

    # Part 1
    print(sum(sum(1 for i in r if i=='1') for r in rows))

    n_groups = sum(1 for _ in find_all_groups(rows))

    return n_groups

if __name__=="__main__":
    example = "flqrgnkx"
    s = input().strip()

    # for r in range(8):
    #     print("".join('#' if i=='1' else '.' for i in row(example, r)[:8]))

    # print(main(example))
    print(main(s))
