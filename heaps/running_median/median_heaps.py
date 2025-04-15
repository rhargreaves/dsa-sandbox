#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def debug(text):
    print(text, file=sys.stderr)


def runningMedian(a):
    lower_half = []
    upper_half = []
    medians = []
    for i in a:
        heapq.heappush(lower_half, -i)
        heapq.heappush(upper_half, -heapq.heappop(lower_half))
        if len(upper_half) > len(lower_half):
            heapq.heappush(lower_half, -heapq.heappop(upper_half))

        max_lower_half = -lower_half[0]
        if len(upper_half) == len(lower_half):
            min_upper_half = upper_half[0]
            median = (min_upper_half + max_lower_half) / 2.0
        else:
            median = max_lower_half
        medians.append(median)
    return medians


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join([f"{r:0.1f}" for r in result]))
    fptr.write('\n')

    fptr.close()
