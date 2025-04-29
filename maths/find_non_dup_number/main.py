from typing import List

# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber_xor(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result

    # 2∗(a+b+c)−(a+a+b+b+c)=c
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
