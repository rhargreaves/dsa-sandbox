# https://www.hackerrank.com/challenges/contacts/problem

import math
import os
import random
import re
import sys

from dataclasses import dataclass, field
#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#


def debug(text):
    print(text, file=sys.stderr)


class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


def insert(root_node, word):
    current_node = root_node
    for c in word:
        if c not in current_node.children:
            current_node.children[c] = Node()
        current_node = current_node.children[c]
    current_node.end_of_word = True  # not really needed if you're just counting the number of words


def count_words_under_node(node):  # naive solution that is more inefficent that the augmented solution
    words = 0
    if node.end_of_word:
        words += 1
    for k, v in node.children.items():
        words += count_words_under_node(v)
    return words


def find(root_node, text):
    current_node = root_node
    for c in text:
        if c in current_node.children:
            current_node = current_node.children[c]
        else:
            return 0
    return count_words_under_node(current_node)


def contacts(queries):
    results = []
    root_node = Node()

    for q in queries:
        cmd = q[0]
        arg = q[1]
        if cmd == "add":
            debug(f"adding name '{arg}'")
            insert(root_node, arg)
            continue
        if cmd == "find":
            debug(f"findstr '{arg}'")
            results.append(find(root_node, arg))

    return results

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
