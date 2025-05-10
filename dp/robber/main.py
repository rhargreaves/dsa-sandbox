from typing import List

# 198. House Robber
# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp_cache(i):
            if i not in memo:
                memo[i] = dp(i)
            return memo[i]

        def dp(i):
            if i > len(nums) - 1:
                return 0

            return nums[i] + max(dp_cache(i + 2), dp_cache(i + 3))

        return max(dp_cache(0), dp_cache(1))
