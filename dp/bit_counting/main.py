from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0 or i == 1:
                dp[i] = i
            else:
                dp[i] = dp[i // 2] + dp[i % 2]
        return dp

    def countBits_naive(self, n: int) -> List[int]:
        results = []
        for i in range(n + 1):
            one_bits = 0
            a = i
            while a != 0:
                if a & 1 == 1:
                    one_bits += 1
                a >>= 1
            results.append(one_bits)
        return results
