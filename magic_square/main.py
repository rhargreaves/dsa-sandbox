#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)


def formingMagicSquare(square):
    valid_squares = []
    squares = permutations(range(1, 10))
    for s in squares:
        if s[0] + s[4] + s[8] != 15 or \
                s[6] + s[4] + s[2] != 15:
            continue
        if s[0] + s[1] + s[2] != 15 or \
            s[3] + s[4] + s[5] != 15 or \
                s[6] + s[7] + s[8] != 15:
            continue
        if s[0] + s[3] + s[6] != 15 or \
            s[1] + s[4] + s[7] != 15 or \
                s[2] + s[5] + s[8] != 15:
            continue
        valid_squares.append(s)

    debug(valid_squares=len(valid_squares))

    lowest_cost = 45
    lowest_square = None
    for v in valid_squares:
        i = 0
        cost = 0
        for r in square:
            for c in r:
                diff = c - v[i]
                cost += abs(diff)
                i += 1
        if cost < lowest_cost:
            lowest_cost = cost
            lowest_square = v

    debug(lowest_square=lowest_square)
    return lowest_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
