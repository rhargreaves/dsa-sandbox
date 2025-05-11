from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(len(nums) - 2):
            for j in range(i, len(nums) - 1):
                for k in range(j, len(nums)):
                    if i < j and j < k:
                        val = (nums[i] - nums[j]) * nums[k]
                        max_val = max(val, max_val)
        return max(0, max_val)
