#!/usr/bin/env python3

import numpy as np

memory = dict()

actions = dict()
def action(f):
    actions[f.__name__] = f

@action
def inc(register, param, reg, c, y):
    if condition(reg, c, y):
        memory[register] = memory.get(register, 0) + param

@action
def dec(register, param, reg, c, y):
    if condition(reg, c, y):
        memory[register] = memory.get(register, 0) - param

comparison_f = dict()
comparison_f['>'] = lambda x, y: x>y
comparison_f['>='] = lambda x, y: x>=y
comparison_f['<='] = lambda x, y: x<=y
comparison_f['<'] = lambda x, y: x<y
comparison_f['=='] = lambda x, y: x==y
comparison_f['!='] = lambda x, y: x!=y

def condition(reg, c, y):
    return comparison_f[c](memory.get(reg, 0), y)

def parse(line):
    s = line.strip().split()
    reg, command, x, fi, reg_c, c, y = s
    assert fi == "if"
    return command, reg, int(x), reg_c, c, int(y)

def execute(*args):
    actions[args[0]](*args[1:])

def main(fname):
    with open(fname, 'r') as f:
        for line in f:
            # print(parse(line))
            execute(*parse(line))

            yield max(memory.values(), default=0)

    print("Final max:",max(memory.items(), key=lambda x: x[1]))

if __name__=="__main__":
    import sys
    m = max(main(sys.argv[1]))
    print("Max at any time:", m)
