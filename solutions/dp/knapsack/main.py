#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def unboundedKnapsack(k, arr):
    sys.setrecursionlimit(25000)

    memo = {}

    def solve(k, arr):
        if k == 0:
            return 0    # valid
        if k < 0:
            return None  # invalid

        max_total = 0
        for i in arr:
            if k - i in memo:
                total = memo[k - i]
            else:
                total = solve(k - i, arr)
                memo[k - i] = total
            if total is not None:
                max_total = max(total + i, max_total)
        return max_total

    return solve(k, arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for i in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')
    fptr.close()
