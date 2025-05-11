# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

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


# this has a bug even though it passed on HackerRank
# "aadddeee" returns YES (which is wrong)
# see better_solution.py
def isValid(s):
    freqs = defaultdict(int)
    for c in s:
        freqs[c] += 1
    all_freqs = [n for n in freqs.values()]
    debug(f"all_freqs={all_freqs}")

    freqs_of_freqs = defaultdict(int)
    for f in all_freqs:
        freqs_of_freqs[f] += 1
    debug(f"freqs_of_freqs={freqs_of_freqs}")

    if len(freqs_of_freqs) == 1:
        debug("freqs_of_freqs == 1")
        return "YES"

    if len(freqs_of_freqs) > 2:
        debug("More than 2 types of frequencies")
        return "NO"

    ff = list(sorted(freqs_of_freqs.items(), key=lambda k: k[0]))
    lower_freq = ff[0]
    upper_freq = ff[1]

    debug(f"ff={ff}")
    if lower_freq[0] + 1 == upper_freq[0] and (upper_freq[1] == 1):
        return "YES"
    elif lower_freq[1] == 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
