from typing import List


# Trie approach here would be more efficient if we have a lot of queries
# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        cur_prefix = ""
        while True:
            letters = set()
            word_over = False
            for word in strs:
                if i < len(word):
                    letters.add(word[i])
                else:
                    word_over = True
                    break

            if not word_over and len(letters) == 1:
                cur_prefix += letters.pop()
            else:
                break
            i += 1

        return cur_prefix
