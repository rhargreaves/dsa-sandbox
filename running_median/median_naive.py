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
    running_nums = []
    medians = []
    for i in a:
        running_nums.append(i)
        running_nums.sort()
        length = len(running_nums)
        is_even = length % 2 == 0
        debug(f"i = {i}, length = {length}, is_even = {is_even}, length//2 = {length//2}")
        median = 0
        if length != 0:
            floor_half_length = length//2
            if is_even:
                median = (running_nums[floor_half_length - 1] +
                          running_nums[floor_half_length]) / 2.0
            else:
                median = float(running_nums[floor_half_length])
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
