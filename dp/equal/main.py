#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def equal(arr):
    sys.setrecursionlimit(250000)

    memo = {}

    def solve(diff):
        if diff == 0:
            return 0

        min_ops = sys.maxsize
        for dec in [1, 2, 5]:
            if diff - dec < 0:
                continue
            if diff - dec in memo:
                ops = memo[diff - dec] + 1
            else:
                memo[diff - dec] = solve(diff - dec)
                ops = memo[diff - dec] + 1
            min_ops = min(ops, min_ops)
        return min_ops

    total_ops = sys.maxsize
    min_val = min(arr)
    for norm_val in range(min_val, min_val-4, -1):
        norm_ops = 0
        for i in range(len(arr)):
            n = arr[i] - norm_val
            if n < 0:
                norm_ops = sys.maxsize
                break
            if n not in memo:
                memo[n] = solve(n)
            norm_ops += memo[n]
        total_ops = min(total_ops, norm_ops)
    return total_ops


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
