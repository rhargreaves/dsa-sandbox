
# solution for https://www.hackerrank.com/challenges/balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# original solution


def isBalanced(s):
    tokens = []
    for c in s:
        if c in "([{":
            tokens.append(c)
        if c in ")]}":
            if len(tokens) == 0:
                return "NO"
            popped_c = tokens.pop()
            if (c == ")" and popped_c != "(") or \
                (c == "]" and popped_c != "[") or \
                    (c == "}" and popped_c != "{"):
                return "NO"
    return "YES" if len(tokens) == 0 else "NO"


# alternative solution
def isBalanced(s):
    tokens = []
    matched_pairs = {
        '(': ')',
        "{": "}",
        "[": "]"
    }
    for c in s:
        if c in "([{":
            tokens.append(c)
        if c in ")]}":
            if len(tokens) == 0:
                return "NO"
            opener = tokens.pop()
            if opener in matched_pairs and matched_pairs[opener] != c:
                return "NO"
    return "YES" if len(tokens) == 0 else "NO"


# better solution
def isBalanced(s):
    tokens = []
    matched_pairs = {
        '(': ')',
        "{": "}",
        "[": "]"
    }
    for c in s:
        if c in matched_pairs.keys():
            tokens.append(c)
        if c in matched_pairs.values():
            if len(tokens) == 0:
                return "NO"
            opener = tokens.pop()
            if opener in matched_pairs and matched_pairs[opener] != c:
                return "NO"
    return "YES" if len(tokens) == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
