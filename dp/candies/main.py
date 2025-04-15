#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()),
          file=sys.stderr)


def candies(n, arr):
    debug("start", arr=arr)
    last_candies = 0
    last_score = arr[0]
    candies = [1] * len(arr)
    for i in range(len(arr)):
        if arr[i] > last_score:
            last_candies += 1
        else:
            last_candies = 1
        last_score = arr[i]
        candies[i] = last_candies

    debug("pass 1", candies=candies)

    last_score = arr[-1]
    last_candies = candies[-1]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > last_score and not candies[i] > last_candies:
            candies[i] = last_candies + 1
        last_candies = candies[i]
        last_score = arr[i]
    debug("pass 2", candies=candies)

    return sum(candies)

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
