#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)


def kangaroo(x1, v1, x2, v2):
    debug(x1=x1, v1=v1, x2=x2, v2=v2)

    if v1 == v2:  # needed to avoid div/0 below
        if x1 != x2:
            return "NO"
        else:
            return "YES"

    # if x1 + v1*t == x2 + v2*t (and t is a +ve int, then they meet)
    # v1*t - v2*t = x2 - x1
    # t(v1 - v2) = x2 - x1
    t = (x2 - x1) / (v1 - v2)
    return "YES" if t >= 0 and t.is_integer() else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
