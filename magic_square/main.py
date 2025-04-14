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
        # centre must be 5
        if s[4] != 5:
            continue
        # diagnonals
        if s[0] + s[4] + s[8] != 15 or \
                s[6] + s[4] + s[2] != 15:
            continue
        # rows
        if not all(sum(s[i:i+3]) == 15 for i in range(0, 9, 3)):
            continue
        # cols
        if not all(s[i] + s[i+3] + s[i+6] == 15 for i in range(0, 3)):
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
