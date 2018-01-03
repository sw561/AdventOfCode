#!/usr/bin/env python3

from math import sqrt

def read(fname):
    particles = []
    i = 0
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip().replace('>', '<')
            particles.append([i])
            i += 1
            for u in line.split('<')[1::2]:
                particles[-1].append(tuple(int(x) for x in u.split(',')))

    # for p in particles:
    #   print(p)
    return particles

def main(fname):
    particles = read(fname)

    # Part 1
    # Find minimum manhatten acceleration
    #
    def manhatten_acceleration(p):
        return tuple(sum(abs(x) for x in u) for u in p[3:0:-1])

    pmin = min(particles, key=manhatten_acceleration)
    print(pmin[0])

    destroyed = set()
    for p1, p2, t in get_collisions(particles):
        destroyed.add(p1)
        destroyed.add(p2)

    print(len(particles) - len(destroyed))

def get_collisions(particles):
    # Get time solutions for x-coords, then check if they will also match in y
    # and z.
    #
    # x1(t) = x1 + v1 * t + a1 * t * (t+1) / 2

    # x2(t) = x2 + v2 * t + a2 * t * (t+1) / 2

    # x1(t) = x2(t) =>
    #
    #   x1 - x2 + (v1-v2) * t + (a1/2 - a2/2) * t + (a1/2 - a2/2) * t**2 = 0
    #
    #   quadratic equation with a = a1 - a2
    #                           b = 2*(v1-v2) + a1 - a2
    #                           c = 2*(x1-x2)
    def pos(particle, index, t):
        return particle[1][index] + particle[2][index]*t + particle[3][index]*t*(t+1)//2

    for p1 in particles:
        for p2 in particles:
            if p1[0]==p2[0]:
                break

            x1 = p1[1][0]
            x2 = p2[1][0]

            v1 = p1[2][0]
            v2 = p2[2][0]

            a1 = p1[3][0]
            a2 = p2[3][0]

            # Times for matching x coords
            for t in pos_ints(quadratic_equation_solver(a1-a2, a1-a2 + 2*(v1-v2), 2*(x1-x2))):
                # Check matching y and z coords
                if all(pos(p1, index, t)==pos(p2, index, t) for index in [1,2]):
                    yield p1[0], p2[0], t
                    break

def quadratic_equation_solver(a, b, c):
    # Looking for real solutions only!!
    if a==0:
        if b==0: return
        # solve b*x + c = 0
        yield -c / b
        return

    d = b*b - 4*a*c
    if d < 0: return

    u = sqrt(d)
    if abs(int(u)-u) > 1e-10:
        return

    yield (-b-u) / (2*a)
    yield (-b+u) / (2*a)

def pos_ints(it):
    for x in it:
        u = int(x)
        if u > 0 and abs(u-x) < 1e-10:
            yield u

if __name__=="__main__":
    import sys
    main(sys.argv[1])
