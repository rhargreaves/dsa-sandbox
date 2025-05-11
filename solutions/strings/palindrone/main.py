import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False

        return True

    def isPalindrome_numeric_operations_only(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        num_digits = math.floor(math.log(x, 10)) + 1

        def nth_digit(x, n):
            y = math.pow(10, n)
            return (x % y) // (y / 10)

        for n in range(num_digits, 0, -1):
            if nth_digit(x, n) != nth_digit(x, num_digits - n + 1):
                return False
        return True
