#!/bin/python3

# https://www.hackerrank.com/challenges/encryption/problem

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)


def encryption(s):
    len_s = len(s)
    len_sqrt = math.sqrt(len_s)
    rows = math.floor(len_sqrt)
    cols = math.ceil(len_sqrt)
    if rows * cols < len_s:
        rows += 1
    debug(len_s=len_s, rows=rows, cols=cols)

    row = 0
    col = 0
    grid = [[' ']*cols for i in range(rows)]
    for i in range(len_s):
        debug("grid", i=i, row=row, col=col, c=s[i])
        grid[row][col] = s[i]
        col += 1

        if col > cols-1:
            debug("looping", cols=cols, col=col)
            col = 0
            row += 1
    debug(grid=grid)

    msg = ''
    for c in range(cols):
        for r in range(rows):
            t = grid[r][c]
            if t != ' ':
                msg += t
            if r == (rows-1):
                msg += ' '

    return msg


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
