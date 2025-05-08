# https://leetcode.com/problems/find-the-difference


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_hash = {}
        for c in s:
            s_hash[c] = s_hash.get(c, 0) + 1

        for c in t:
            if c not in s_hash:
                return c
            else:
                s_hash[c] -= 1
                if s_hash[c] == 0:
                    del s_hash[c]

        return list(s_hash.keys())[0]
