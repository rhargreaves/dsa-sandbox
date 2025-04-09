#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

cache = {}

def getWaysCached(amount, denoms):
    key = (amount, denoms[0] if denoms else None)
    if key in cache:
        return cache[key]
    else:
        ways = getWays(amount, denoms)
        cache[key] = ways
        return ways

def getWays(amount, denoms):
    if amount == 0:
        return 1
    if amount < 0 or len(denoms) == 0:
        return 0
    return getWaysCached(amount - denoms[0], denoms) + getWaysCached(amount, denoms[1:])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    print(f"Cache size = {len(cache)}", file=sys.stderr)

    fptr.write(str(ways) + '\n')

    fptr.close()
