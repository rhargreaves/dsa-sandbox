# https://www.hackerrank.com/challenges/reduced-string/problem

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def superReducedString(s):
    i = 0
    while i < len(s)-1:
        c = s[i]
        if s[i+1] == c:
            s = s[:i] + s[i+2:]
            i = 0
            continue
        i += 1

    if s == '':
        return 'Empty String'
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
