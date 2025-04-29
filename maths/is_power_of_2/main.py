# https://leetcode.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        return (n - 1) & n == 0


# e.g. 4 = 0100,  3 = 0011, 4 & 3 = 0000
#      8 = 1000,  7 = 0111, 8 & 7 = 0000
