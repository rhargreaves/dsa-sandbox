import sys


def debug(context="", **kwargs):
    print(
        (context + ": " if context else "")
        + " ".join(f"{k}={v}" for k, v in kwargs.items()),
        file=sys.stdout,
    )


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validPalindromeRange(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return validPalindromeRange(s, i + 1, j) or validPalindromeRange(
                    s, i, j - 1
                )
            i += 1
            j -= 1
        return True
