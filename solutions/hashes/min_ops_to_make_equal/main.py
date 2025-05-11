# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        sorted_nums = sorted(num_set)

        if k > sorted_nums[0]:
            return -1

        if k == sorted_nums[0]:
            return len(sorted_nums) - 1
        else:
            return len(sorted_nums)
