#!/usr/bin/env python3

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

# Need to find manhattan distance to centre from a given number

# Find number of nodes in each square whose sides increase by 2
#
# This is 8 * i
#
# 1, 8, 16, 24, 32
#
# The nodes add each time
#
# So at distance 0: 1  -> 1
#    at distance 1: 2  -> 9       2  4  6  8
#    at distance 2: 10 -> 25     11 15 19 23
#    at distance 3: 26 -> 49     28 34 40 46
#    at distance 4: 50 -> 81     53 61 69 77

def distance(x):
    d = 0
    while (2*d+1)**2 < x:
        d += 1

    first = (2*d-1)**2 + 1

    sides = [first + d-1 + 2*d*i for i in range(4)]

    distance_to_closest_side = min(abs(side-x) for side in sides)

    return distance_to_closest_side + d

for u in [1, 12, 23, 1024]:
    print("u, distance(u):", u, distance(u))

x = 277678
print("distance(x):", distance(x))
