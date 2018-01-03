#!/usr/bin/env python3

def str_pattern(pattern):
    return "\n".join("".join(x for x in row) for row in pattern)

def print_pattern(pattern):
    print(str_pattern(pattern))

def rotate(pattern):
    newp = []

    # Write first row using first column
    for row in range(len(pattern)):
        newp.append([])
        for i in range(len(pattern)-1,-1,-1):
            newp[-1].append(pattern[i][row])

    return newp

def reflect(pattern):
    # Reflect pattern about line vertical line, x=0
    newp = []

    for row in range(len(pattern)):
        newp.append([])
        for col in range(len(pattern)-1,-1,-1):
            newp[-1].append(pattern[row][col])

    return newp

def versions(pattern):
    # Get all versions: all four rotations for original and flipped

    for j in range(2):
        p = pattern
        if j==1:
            p = reflect(p)

        yield p
        for i in range(3):
            p = rotate(p)
            yield p

def get_patterns(fname):
    d = dict()

    with open(fname, 'r') as f:
        for line in f:
            line = line.replace('>','')
            pt = line.split('=')
            p, t = (list(map(list, x.strip().split('/'))) for x in pt)

            for x in versions(p):
                d[str_pattern(x)] = t

    return d

def blockify(image, block_size):
    blocks = []
    for row in range(0, len(image), block_size):
        blocks.append([])
        for col in range(0, len(image), block_size):
            blocks[-1].append([])
            for x in range(block_size):
                blocks[-1][-1].append([])
                for y in range(block_size):
                    blocks[-1][-1][-1].append(image[row+x][col+y])
    return blocks

def unblock(blocks):
    block_size = len(blocks[0][0])
    image = []
    for blocki in range(len(blocks)):
        for row in range(block_size):
            image.append([])
            for blockj in range(len(blocks)):
                for col in range(block_size):
                    image[-1].append(blocks[blocki][blockj][row][col])
    return image

def enhance(image, patterns):
    if len(image)%2 == 0:
        blocks = blockify(image, 2)
    elif len(image)%3 == 0:
        blocks = blockify(image, 3)
    else:
        print("help")

    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            blocks[i][j] = patterns[str_pattern(blocks[i][j])]

    return unblock(blocks)

def count_on(image):
    c = 0
    for row in image:
        for pixel in row:
            if pixel=='#':
                c += 1
    return c

def main(argv):

    d = get_patterns(argv)

    # for key in d:
    #   print("key, d[key]:\n{}\n{}".format(key, str_pattern(d[key])))

    im = []
    with open("start", 'r') as f:
        for line in f:
            im.append(list(line.strip()))

    # print_pattern(im)

    for u in range(18):
        im = enhance(im, d)
        # print("---------------------")
        # print_pattern(im)

        if u in [4,17]:
            print("After {:2d} iterations, number of pixels on: {}".format(
                (u+1), count_on(im)
                ))

if __name__=="__main__":
    import sys
    main(sys.argv[1])
