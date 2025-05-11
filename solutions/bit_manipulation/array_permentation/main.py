from typing import List

# https://leetcode.com/problems/build-array-from-permutation


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] | ((nums[(nums[i] & 0xFFFF)] & 0xFFFF) << 16)
        for i in range(len(nums)):
            nums[i] = nums[i] >> 16
        return nums
