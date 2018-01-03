#!/usr/bin/env python3

def parse(line):
    line = line.replace('<-', '')

    p, c = line.split('>')
    p = int(p)
    c = [int(ci) for ci in c.split(',')]

    return p, c

def find_tree(edges, node):

    nodes = set([node])
    nodes_to_add = [node] # Stack of nodes to add

    while nodes_to_add:
        node = nodes_to_add.pop()

        for ci in edges[node]:
            if ci not in nodes:
                nodes_to_add.append(ci)
                nodes.add(ci)

    return nodes

def find_all_groups(edges):

    visited = set()
    for node in edges.keys():
        if node not in visited:
            group = find_tree(edges, node)
            yield group
            visited.update(group)

if __name__=="__main__":
    import sys
    fname = sys.argv[1]

    edges = dict()
    with open(fname, 'r') as f:
        for line in f:
            parent, children = parse(line)
            edges[parent] = children

    # Part 1
    nodes = find_tree(edges, 0)
    print("Number of nodes in group with node 0:", len(nodes))

    # Part 2
    c = sum(1 for g in find_all_groups(edges))
    print("Number of groups:", c)
