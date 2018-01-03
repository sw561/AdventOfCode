#!/usr/bin/env python3

def reallocate(u):
    i, xi = max(enumerate(u), key=lambda x: (x[1], -x[0]))

    u[i] = 0
    for ni in range(i+1, i+1+xi):
        u[ni%len(u)] += 1

def solve(f):
    u = [int(x) for x in next(f).split()]
    visited = dict()
    steps = 0

    while tuple(u) not in visited:
        # print("Step: {}, u={}".format(steps, u))
        visited[tuple(u)] = steps
        reallocate(u)
        steps += 1
    print("Step: {}, u={}".format(steps, u))

    return steps, visited[tuple(u)]

if __name__=="__main__":
    import sys
    with open(sys.argv[1], 'r') as f:
        n, step_matching = solve(f)
    print("Number of steps: {}".format(n))
    print("Size of loop: {}".format(n-step_matching))
