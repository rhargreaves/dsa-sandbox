from typing import List


class Node:
    def __init__(self):
        self.letters = [None] * 26
        self.count = 0
        self.end_of_word = False


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Node()

        for word in strs:
            node = root
            for i, c in enumerate(word):
                key = ord(c) - ord("a")
                if node.letters[key] is None:
                    node.letters[key] = Node()
                    node.count += 1
                node = node.letters[key]
            node.end_of_word = True

        prefix_len = 0
        node = root
        while node.count == 1 and not node.end_of_word:
            next_node = [n for n in node.letters if n is not None][0]
            node = next_node
            prefix_len += 1

        return strs[0][0:prefix_len]
