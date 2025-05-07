import sys
from typing import List

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def is_sorted(nums):
            prev = None
            for n in nums:
                if prev is None:
                    prev = n
                if prev > n:
                    return False
                prev = n
            return True

        attempts = 0
        while not is_sorted(nums):
            min_sum = sys.maxsize
            min_sum_at = -1
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_sum_at = i
            if min_sum_at != -1:
                nums.pop(min_sum_at)
                nums[min_sum_at] = min_sum
                attempts += 1
        return attempts
