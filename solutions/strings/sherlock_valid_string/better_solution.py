#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def debug(text):
    print(text, file=sys.stderr)

def isValid(s):
    freqs = defaultdict(int)
    for c in s:
        freqs[c] += 1
    all_freqs = [n for n in freqs.values()]
    debug(f"all_freqs={all_freqs}")

    count_of_freqs = defaultdict(int)
    for f in all_freqs:
        count_of_freqs[f] += 1
    debug(f"count_of_freqs={count_of_freqs}")

    if len(count_of_freqs) == 1:
        debug("count_of_freqs == 1")
        return "YES"

    if len(count_of_freqs) > 2:
        debug("More than 2 frequencies")
        return "NO"

    cf = list(sorted(count_of_freqs.items(), key=lambda k: k[0]))
    lower_freq = cf[0]
    upper_freq = cf[1]

    debug(f"cf={cf}")
    if lower_freq[0] + 1 == upper_freq[0] and upper_freq[1] == 1:
        debug("gap of 1 between counts and upper freq count = 1")
        return "YES"
    elif lower_freq[0] == 1 and lower_freq[1] == 1:
        debug("lower freq (1) has count 1")
        return "YES"
    else:
        debug("else")
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
