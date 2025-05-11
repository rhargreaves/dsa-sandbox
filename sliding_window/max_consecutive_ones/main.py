from typing import List


# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        max_length = 0
        zeroes = 0
        for i in range(len(nums)):  # fast pointer
            if nums[i] == 0:
                zeroes += 1

            while zeroes > k:  # too many zeros; shrink window
                if nums[j] == 0:
                    zeroes -= 1
                j += 1  # slow pointer

            max_length = max(i - j + 1, max_length)
        return max_length
