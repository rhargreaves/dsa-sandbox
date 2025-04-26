from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 0
        w = 0
        last_num = None
        while r < len(nums):
            if nums[r] != last_num:
                nums[w] = nums[r]
                w += 1

            last_num = nums[r]
            r += 1

        return w
