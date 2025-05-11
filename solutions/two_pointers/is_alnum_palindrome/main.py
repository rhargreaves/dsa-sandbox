class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < len(s) and j >= 0:  # can just be i < j
            ic = s[i].lower()
            if not ic.isalnum():
                i += 1
                continue

            jc = s[j].lower()
            if not jc.isalnum():
                j -= 1
                continue

            if ic != jc:
                return False

            i += 1
            j -= 1

        return True
