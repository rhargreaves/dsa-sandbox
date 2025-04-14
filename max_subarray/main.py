#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()),
          file=sys.stderr)


def maxSubarray(arr):
    # subsequence = any combination
    # subarray = contiguous
    freqs = Counter(arr)
    debug(freqs=freqs)
    unique_vals = sorted(freqs.keys(), reverse=True)
    debug(unique_vals=unique_vals)
    maxSubsequence = 0
    if unique_vals[0] < 0:
        maxSubsequence = unique_vals[0]
    else:
        for v in unique_vals:
            if v > 0:
                maxSubsequence += freqs[v] * v

    max_sum = -sys.maxsize
    cur_sum = -sys.maxsize
    for start in range(len(arr)):
        s = arr[start]
        if cur_sum + s < s:
            cur_sum = s
        else:
            cur_sum += s
        if cur_sum > max_sum:
            max_sum = cur_sum
    maxSubarray = max_sum

    # Write your code here
    return [maxSubarray, maxSubsequence]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
