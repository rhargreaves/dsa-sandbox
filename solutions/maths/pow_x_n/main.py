# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # x^0 == 1
        if n < 0:
            n = -n
            x = 1 / x  # x^-n == 1 / x^n
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)  # (x^2)^(n/2) == x^n
        else:
            return x * self.myPow(x, n - 1)  # x * x^(n-1) == x^n
