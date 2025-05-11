class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        x = n
        while x % 3 == 0:
            x /= 3

        return x == 1
