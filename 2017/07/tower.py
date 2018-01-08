#!/usr/bin/env python3

from pprint import pprint

def parse(line):
    line = line.strip()
    line = line.replace(')', '')
    line = line.replace('>', '(')
    line = line.replace('-', '')
    line = line.replace(',', '')
    s = line.split('(')

    if len(s) > 2:
        name, w, c = s
        c = c.split()
    else:
        name, w = s
        c = []
    name = name.strip()
    w = int(w)

    return name, w, c

def find_root(parents):
    node = next(iter(parents))

    while node in parents:
        node = parents[node]

    return node

def total_weight(node, children, weight):
    def total_weight_(node):
        w = weight[node]
        for ci in children[node]:
            w += total_weight_(ci)
        return w
    return total_weight_(node)

def rebalance(root, children, weight):
    node = root
    while True:
        cw = [(ci, total_weight(ci, children, weight)) for ci in children[node]]

        print("cw:", cw)

        assert len(cw) != 2

        d = dict()
        for (x, w) in cw:
            d[w] = d.get(w, [])
            d[w].append(x)

        d = sorted(d.items(), key=lambda x: len(x[1]))

        if len(d)==2:
            node = d[0][1][0] # i.e. check the node which is unlike the others
            desired_weight = d[1][0]
            actual_weight = d[0][0]
        else:
            return node, actual_weight, desired_weight

def main(fname):

    # children[pname] returns a list of programs above pname
    children = dict()
    # weight[pname] is the weight of pname
    weight = dict()
    # parent[pname] returns the program below pname
    parents = dict()

    with open(fname, 'r') as f:
        for line in f:
            name, w, c = parse(line)

            children[name] = c
            weight[name] = w

            for ci in c:
                parents[ci] = name

    # pprint(children)
    # pprint(parents)

    root = find_root(parents)
    # Part 1
    print("Parent: {}".format(root))

    # Part 2
    # Change the weight of one node, such that everything is balanced

    node, actual_weight, desired_weight = rebalance(root, children, weight)
    print("node, actual_weight, desired_weight:", node, actual_weight, desired_weight)
    print("own weight: {}".format(weight[node]))
    print("new weight: {}".format(weight[node] + desired_weight - actual_weight))

if __name__=="__main__":
    import sys
    main(sys.argv[1])
