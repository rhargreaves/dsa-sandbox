# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

import math
import os
import random
import re
import sys
import queue

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def debug(text):
    print(text, file=sys.stderr)


def build(indexes, root_node):
    q = queue.Queue()
    q.put(root_node)
    while not q.empty():
        if indexes:
            pair = indexes.pop(0)
        else:
            break
        debug(f"pair={pair}")
        left_val = pair[0]
        right_val = pair[1]
        node = q.get()
        if left_val != -1:
            node.left = Node(left_val)
            q.put(node.left)
        if right_val != -1:
            node.right = Node(right_val)
            q.put(node.right)


def walk_n_swap(node, k, level):
    debug(f"walk: {node.value}, k = {k}, level = {level}")
    if node.left:
        walk_n_swap(node.left, k, level + 1)
    if node.right:
        walk_n_swap(node.right, k, level + 1)
    is_multiple = level % k == 0
    if is_multiple:
        debug(f"is_multiple: {is_multiple} for {node.value}, k={k}, level={level}")
        left = node.left
        node.left = node.right
        node.right = left


def traverse(node, result):
    if node.left:
        traverse(node.left, result)
    result.append(node.value)
    if node.right:
        traverse(node.right, result)


def swapNodes(indexes, queries):
    sys.setrecursionlimit(15000)  # needed otherwise test case 10 & 11 fail
    root_node = Node(1)
    build(indexes, root_node)
    output = []
    for q in queries:
        walk_n_swap(root_node, q, 1)
        result = []
        traverse(root_node, result)
        output.append(result)

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
