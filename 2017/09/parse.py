#!/usr/bin/env python3

def remove_bang(s):
    # Remove exclamation marks and what follows them
    # s is an iterator
    while True:
        try:
            u = next(s)
        except StopIteration:
            return

        if u=='!':
            next(s)
        else:
            yield u

def remove_garbage(s):
    # Yield characters excluding all the garbage
    # Also count the garbage as we are going

    garbage_count = 0

    while True:
        try:
            u = next(s)
        except StopIteration:
            break

        if u=="<":
            while u!=">":
                u = next(s)
                garbage_count += 1
            garbage_count -= 1
        else:
            yield u

    print("garbage_count:", garbage_count)

def find_groups(s):
    # Find total score of group starting at index i with given score
    # Nested groups will have score + 1

    def find_groups_(i, score):
        # print("i, score:", i, score)

        j = i+1
        x = score
        while s[j]!='}':
            if s[j] == '{':
                xx, j = find_groups_(j, score+1)
                x += xx
            j += 1

        # print("Called with {}, {} and return {}, {}".format(i, score, x, j))
        return x, j

    x, j = find_groups_(0, 1)
    return x

if __name__=="__main__":
    s = input()

    s = "".join(remove_garbage(remove_bang(iter(s))))
    # print("s:", s)

    score = find_groups(s)

    print("score:", score)
