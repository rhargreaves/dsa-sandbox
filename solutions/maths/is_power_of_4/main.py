class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        if (n - 1) & n == 0:  # power of 2
            return n & 0x55555555 == n
        return False
