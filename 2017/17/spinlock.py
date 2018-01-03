#!/usr/bin/env python3

def spin(n):

    u = [0]
    pos = 0

    for i in range(1, 2018):
        pos = (pos+n)%len(u)

        u.insert(pos+1, i)
        pos += 1

    print("u[:5]:", u[:5])

    return u

def part1(n):
    u = spin(n)
    # print("u:", u)

    x = u.index(2017)

    print(u[x-3:x+4])

    return u[x+1]

def spin_fast(nstep, niter=2018):
    pos = 0
    lenu = 1
    final_i = 0
    for i in range(1, niter):
        pos = (pos+nstep)%lenu
        if pos==0:
            final_i = i
        lenu += 1
        pos = (pos+1)%lenu
    return final_i

if __name__=="__main__":
    # example
    x = part1(3)
    print("Example", x)

    x = part1(335)
    print("Part 1", x)

    # print("Practice for part 2")
    # x = spin_fast(3)
    # print("Example", x)
    # x = spin_fast(335)
    # print("With Input", x)

    x = spin_fast(335, int(50e6))
    print("Part 2", x)
