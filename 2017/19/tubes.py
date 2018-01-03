#!/usr/bin/env python3

def get_map(fname):
    m = []
    with open(fname, 'r') as f:
        for line in f:
            m.append(line[:-1])

    # print("\n".join(m))
    return m

def right_left(dx, dy):
    if dx==0:
        yield -1, 0
        yield 1, 0
    elif dy==0:
        yield 0, -1
        yield 0, 1

def follow(m):
    px = 0
    py = 0
    while m[py][px] == " ":
        px += 1

    dx = 0
    dy = 1

    nsteps = 1

    while True:
        while m[py+dy][px+dx] != ' ':
            py += dy
            px += dx
            nsteps += 1

            if ord('A') <= ord(m[py][px]) <= ord('Z'):
                yield m[py][px]

        # print("px+1, py+1:", px+1, py+1)

        # Check left and right directions for paths
        for dx, dy in right_left(dx, dy):
            if m[py+dy][px+dx] != ' ':
                break
        else:
            break

    yield " {}".format(nsteps)

def main(fname):
    m = get_map(fname)

    print("".join(x for x in follow(m)))

if __name__=="__main__":
    import sys
    main(sys.argv[1])
