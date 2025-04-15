# solution for https://www.hackerrank.com/challenges/tree-top-view/

import sys


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def debug(text):
    print(text, file=sys.stderr)


def topView(root):
    output = []
    h_dists = {}

    # trick is to keep track of level as well as horizontal distance
    # we want to overwrite lower level horizontal distances with top ones!
    def walk(node, h_dist, level):
        if (h_dist not in h_dists) or h_dists[h_dist][1] > level:
            debug(f"node = {node.info}, h_dist = {h_dist}")
            h_dists[h_dist] = (node.info, level)
        if node.left:
            walk(node.left, h_dist - 1, level + 1)
        if node.right:
            walk(node.right, h_dist + 1, level + 1)

    walk(root, 0, 0)

    for k, v in sorted(h_dists.items(), key=lambda i: i[0]):
        output.append(v[0])

    print(" ".join(map(str, output)))


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
