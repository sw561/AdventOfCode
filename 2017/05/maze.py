#!/usr/bin/env python3

PART2 = False

def proceed(maze):
    i = 0
    steps = 0
    while 0 <= i < len(maze):
        new_i = i + maze[i]
        if not PART2 or maze[i]<3:
            maze[i] += 1
        else:
            maze[i] -= 1
        steps += 1
        i = new_i

    return steps

def main(fname):
    with open(fname, 'r') as f:
        maze = []
        for line in f:
            maze.append(int(line))

    print("Number of steps: {}".format(proceed(maze)))

if __name__=="__main__":
    import sys
    main(sys.argv[1])
    print("Part 2")
    PART2 = True
    main(sys.argv[1])
