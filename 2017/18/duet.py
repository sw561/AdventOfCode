#!/usr/bin/env python3

memory = dict((chr(x+ord('a')), 0) for x in range(ord('z')+1-ord('a')))

actions = dict()
def action(f):
    actions[f.__name__] = f

sound = None

def interpret(x):
    try:
        return memory[x]
    except KeyError:
        return int(x)

@action
def snd(i, x):
    global sound
    sound = interpret(x)
    return i+1

@action
def rcv(i, x):
    if interpret(x):
        print("Recovering sound {}".format(sound))
        exit("RRR")
    return i+1

@action
def set(i, x, y):
    memory[x] = interpret(y)
    return i+1

@action
def add(i, x, y):
    memory[x] += interpret(y)
    return i+1

@action
def mul(i, x, y):
    memory[x] *= interpret(y)
    return i+1

@action
def mod(i, x, y):
    memory[x] %= interpret(y)
    return i+1

@action
def jgz(i, x, y):
    if interpret(x)>0:
        return i+interpret(y)
    else:
        return i+1

def read(fname):
    cmds = []
    with open(fname, 'r') as f:
        for line in f:
            cmds.append(line.strip().split())
    return cmds

def main(fname):

    i = 0
    cmds = read(fname)

    while 0 <= i < len(cmds):
        cmd = cmds[i]

        i = actions[cmd[0]](i, *cmd[1:])

if __name__=="__main__":
    import sys
    main(*sys.argv[1:])
