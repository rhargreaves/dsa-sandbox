#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

from collections import defaultdict


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)


def beautifulPairs(a, b):
    seen_a = defaultdict(lambda: 0)
    seen_b = defaultdict(lambda: 0)
    for i in range(len(a)):
        seen_a[a[i]] += 1
        seen_b[b[i]] += 1
    not_in_b = set()
    not_in_a = set()
    for i, f in seen_a.items():
        if i not in seen_b:
            not_in_b.add(i)
    for i, f in seen_b.items():
        if i not in seen_a:
            not_in_a.add(i)

    debug("start", a=a, b=b, seen_a=dict(seen_a), seen_b=dict(seen_b),
          not_in_a=not_in_a, not_in_b=not_in_b)

    existing_pairs = 0
    for i, f in seen_a.items():
        if i in seen_b:
            existing_pairs += min(seen_a[i], seen_b[i])

    if existing_pairs == len(a):
        # already perfect
        # so we need to decrement the counter by 1 to make mandatory change
        return existing_pairs - 1
    else:
        # i.e. len(not_in_a) > 0 or len(not_in_b) > 0:
        return existing_pairs + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
