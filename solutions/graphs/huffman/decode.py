# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

import sys
import queue as Queue

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    msg = ''
    debug(s=s)

    node = root
    while True:
        debug("walk", s=s)
        if not node.left and not node.right:
            msg += node.data
            debug("append, back to root", msg=msg)
            node = root
            if len(s) == 0:
                break
            else:
                continue
        if s[0] == '0':
            s = s[1:]
            debug("moving left")
            node = node.left
        elif s[0] == '1':
            s = s[1:]
            debug("moving right")
            node = node.right
        else:
            debug("shouldn't hit here")
            return

    print(msg)


ip = input()
freq = {}  # maps each character to its frequency

cntr = 0

for ch in ip:
    if (freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1

root = huffman_hidden()  # contains root of huffman tree

code_hidden = {}  # contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:  # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
    toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
