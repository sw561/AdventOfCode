#!/usr/bin/env python3

def turn_left(direction):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    i = directions.index(direction)
    return directions[(i+1)%4]

def add(p, d):
    return (p[0] + d[0], p[1] + d[1])

def get_neighbours(d, pos):
    # Get entries to the dictionary adjacent (including diagonals) to pos
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            yield d.get(add(pos, (dx, dy)), 0)

def create_spiral(imax):
    d = dict() # dict relating positions to numbers

    d[(0, 0)] = 1

    pos = (0, 0)
    direction = (0, -1)

    i = 1

    while True:
        # Add next element to the spiral

        # Try to turn left, if a number is already there go straight
        t_l = turn_left(direction)
        new_pos = add(pos, t_l)
        if new_pos in d:
            new_pos = add(pos, direction)
        else:
            direction = t_l
        pos = new_pos

        if PART2:
            i = sum(get_neighbours(d, pos))
        else:
            i += 1
        d[pos] = i

        if d[pos]>=imax:
            print("{} stored at {} at distance {}".format(d[pos], pos, sum(map(abs, pos))))
            return d

def print_spiral(x):
    d = create_spiral(x)
    for key, x in sorted(d.items(), key=lambda x: x[1]):
        print("{}: {}".format(key, x))

x = 277678

PART2 = False
# print_spiral(23)
d = create_spiral(x)

PART2 = True
# print_spiral(806)
d = create_spiral(x)
