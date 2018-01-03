#!/usr/bin/env python3

# Use a dict to store the locations of the infected nodes, rather then arrays

from itertools import chain

def read(fname):
    d = set()
    with open(fname, 'r') as f:
        for j, line in enumerate(f):
            for i, x in enumerate(line.strip()):
                if x=='#':
                    d.add((i,j))
    pos = j//2
    return d, (pos, pos)

def print_grid(d, weakened, flagged, pos):
    xmin = min(x[0] for x in chain(d, weakened, flagged, [pos]))
    xmax = max(x[0] for x in chain(d, weakened, flagged, [pos]))
    ymin = min(x[1] for x in chain(d, weakened, flagged, [pos]))
    ymax = max(x[1] for x in chain(d, weakened, flagged, [pos]))

    for y in range(ymin, ymax+1):
        g = ""
        for x in range(xmin, xmax+1):
            if (x,y)==pos:
                g += '['
            else:
                g += ' '
            if (x,y) in d:
                g += "#"
            elif (x,y) in weakened:
                g += "W"
            elif (x,y) in flagged:
                g += "F"
            else:
                g += "."
            if (x,y)==pos:
                g += ']'
            else:
                g += ' '

        print(g)

# Use coordinates (x,y) where x is to right, and y is downwards
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn(direction, x):
    return directions[(directions.index(direction) + x) % len(directions)]

def turn_left(direction):
    return turn(direction, 1)

def turn_right(direction):
    return turn(direction, -1)

def turn_back(direction):
    return turn(direction, 2)

def step(pos, direction):
    return tuple(p+d for p, d in zip(pos, direction))

def burst_part1(d, pos, direction):
    if pos in d:
        new_d = turn_right(direction)
        d.remove(pos)
        infection = False
    else:
        new_d = turn_left(direction)
        d.add(pos)
        infection = True

    new_pos = step(pos, new_d)

    return new_pos, new_d, infection

def burst_part2(d, weakened, flagged, pos, direction):
    infection = False
    if pos in d: # infected
        new_d = turn_right(direction)
        d.remove(pos)
        flagged.add(pos)

    elif pos in flagged:
        new_d = turn_back(direction)
        flagged.remove(pos)

    elif pos in weakened:
        new_d = direction
        weakened.remove(pos)
        d.add(pos)
        infection = True

    else:
        new_d = turn_left(direction)
        weakened.add(pos)

    new_pos = step(pos, new_d)

    return new_pos, new_d, infection

def main(argv):
    d, pos = read(argv)
    direction = (0, -1)
    n_infections = 0

    # print_grid(d, pos)
    # print("d:", d)
    # print("pos:", pos)
    # print("direction:", direction)

    for count in range(10000):
        pos, direction, infection = burst_part1(d, pos, direction)
        if infection:
            n_infections += 1
        if count == 69:
            print_grid(d, {}, {}, pos)
    # print("---")
    # print_grid(d, {}, {}, pos)
    print("n_infections:", n_infections)

    d, pos = read(argv)
    weakened = set()
    flagged = set()
    direction = (0, -1)
    n_infections = 0

    for count in range(int(1e7)):
        pos, direction, infection = burst_part2(d, weakened, flagged, pos, direction)
        if infection:
            n_infections += 1
        if count == 6:
            print_grid(d, weakened, flagged, pos)
    print("n_infections:", n_infections)

if __name__=="__main__":
    import sys
    main(sys.argv[1])
