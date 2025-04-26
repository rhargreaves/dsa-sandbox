from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

    def plusOne_naive(self, digits: List[int]) -> List[int]:
        carry = 0
        i = len(digits) - 1

        result = []
        while i >= 0 or carry:
            sum = (
                (digits[i] if i >= 0 else 0)
                + (1 if i == len(digits) - 1 else 0)
                + carry
            )
            carry = sum // 10
            sum %= 10
            result.insert(0, sum)  # warning: O(n) !!
            i -= 1

        return result
