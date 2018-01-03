#!/usr/bin/env python3

directions = {
    'n': (1, 0),
    'ne': (1, 1),
    'se': (0, 1),
    's': (-1, 0),
    'sw': (-1, -1),
    'nw': (0, -1)
    }

def distance(pos):
    # Find shortest distance in hex-grid steps

    distance = 0

    if pos[0] * pos[1] > 0:
        m = min(pos, key=abs)
    else:
        m = 0

    return sum(abs(x) for x in [m, pos[0]-m, pos[1]-m])

def follow_path(ds):
    pos = (0, 0)

    for d in ds:
        p = directions[d]
        pos = pos[0] + p[0], pos[1] + p[1]
        yield pos

    print("Final distance:", distance(pos))

if __name__=="__main__":
    import sys
    f = open(sys.argv[1], 'r')
    ds = next(f).strip().split(',')

    furthest = max(distance(p) for p in follow_path(ds))

    print("furthest:", furthest)
