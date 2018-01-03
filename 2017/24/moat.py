#!/usr/bin/env python3

def read(fname):
    ports = dict()
    with open(fname, 'r') as f:
        for line in f:
            u = tuple(int(x) for x in line.split('/'))
            for a, b in [u, reversed(u)]:
                if a not in ports:
                    ports[a] = dict()
                ports[a][b] = ports[a].get(b, 0) + 1

    return ports

def strength(bridge):
    return 2*sum(bridge[:-1]) + bridge[-1]

def get_bridges(ports, bridge, n):
    extended = False

    for x in ports[n]:
        if ports[n][x] == 0:
            continue
        extended = True

        ports[n][x] -= 1
        ports[x][n] -= 1
        bridge.append(x)

        yield from get_bridges(ports, bridge, x)

        ports[n][x] += 1
        ports[x][n] += 1
        bridge.pop()

    if not extended:
        yield bridge

def main(fname):
    ports = read(fname)
    if fname == "example":
        print("ports:", ports)
        for bridge in get_bridges(ports, [], 0):
            print("bridge:", bridge, strength(bridge))

    part1_strength = 0
    part2_length = 0
    part2_strength = 0

    for bridge in get_bridges(ports, [], 0):
        s = strength(bridge)
        if s > part1_strength:
            part1_strength = s

        if (len(bridge), s) > (part2_length, part2_strength):
            part2_length = len(bridge)
            part2_strength = s

    print(part1_strength)
    print(part2_strength)

if __name__=="__main__":
    import sys
    main(sys.argv[1])
