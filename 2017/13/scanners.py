#!/usr/bin/env python3

def height(r, t):
    # Get the height of scanner with range r after time t

    # It takes (r-1) * 2 to get back to the start
    t %= (r-1)*2

    # It takes r-1 time to reach the bottom
    if t <= r-1:
        return t
    else:
        return 2*(r-1) - t

def severity(scanners, depths):
    s = 0
    for t in depths:
        if height(scanners[t], t)==0:
            s += t * scanners[t]
    return s

def caught(scanners, depths, delay=0):
    for t in depths:
        if height(scanners[t], t+delay)==0:
            return True
    return False

if __name__=="__main__":
    import sys

    scanners = dict()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            depth, r = [int(x) for x in line.replace(':', '').split()]
            scanners[depth] = r

    # For quick checking, check the scanners most likely to catch us first
    depths = sorted(list(scanners.keys()), key=lambda x: scanners[x])

    # Part 1
    print(severity(scanners, depths))

    # Part 2
    delay = 0
    while caught(scanners, depths, delay):
        delay += 1

    print(delay)
