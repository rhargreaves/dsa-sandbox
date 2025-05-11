# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    break

        return j == len(s)
