# https://leetcode.com/problems/sqrtx

# Uses Newton's method rather than strict binary search


class Solution:
    def avg(self, nums):
        return sum(nums) / len(nums)

    def mySqrt(self, x: int) -> int:
        guess = 1
        while abs(guess * guess - x) > 0.1:
            guess = self.avg([guess, x / guess])
        return int(guess)
