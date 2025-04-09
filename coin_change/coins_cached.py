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

def getWays(amount, denoms):
    if amount == 0:
        return 1
    if amount < 0 or len(denoms) == 0:
        return 0

    key = f"{amount - denoms[0]}_{denoms[0] if denoms else None}"
    if key in cache:
        remaining_ways = cache[key]
    else:
        remaining_ways = getWays(amount - denoms[0], denoms)
        cache[key] = remaining_ways

    key = f"{amount}_{denoms[1:][0] if denoms[1:] else None}"
    if key in cache:
        other_coin_ways = cache[key]
    else:
        other_coin_ways = getWays(amount, denoms[1:])
        cache[key] = other_coin_ways

    return remaining_ways + other_coin_ways

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
