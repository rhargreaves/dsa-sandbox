# https://leetcode.com/problems/add-strings


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        result = ""
        while i >= 0 or j >= 0 or carry != 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            sum_digits = n1 + n2 + carry
            carry = sum_digits // 10
            result = str(sum_digits % 10) + result
            i -= 1
            j -= 1
        return result
