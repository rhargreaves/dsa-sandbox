import sys
from typing import List


def debug(context="", **kwargs):
    print(
        (context + ": " if context else "")
        + " ".join(f"{k}={v}" for k, v in kwargs.items()),
        file=sys.stdout,
    )


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findBound(left, right, isLast):
            debug("findBound", left=left, right=right, isLast=isLast)

            if left > right:
                return -1

            index = (left + right) // 2
            if nums[index] == target:
                if (not isLast and index == 0) or (isLast and index == len(nums) - 1):
                    return index
                if (not isLast and nums[index - 1] < target) or (
                    isLast and nums[index + 1] > target
                ):
                    return index

            if (not isLast and nums[index] >= target) or (nums[index] > target):
                return findBound(left, index - 1, isLast)
            else:
                return findBound(index + 1, right, isLast)

        return [findBound(0, len(nums) - 1, False), findBound(0, len(nums) - 1, True)]

    def searchRange_slow(self, nums: List[int], target: int) -> List[int]:

        def solve(left, right):
            if left > right:
                return [-1, -1]

            index = (left + right) // 2
            if nums[index] == target:
                start = index
                end = index
                while start >= 0 and nums[start] == nums[index]:
                    start -= 1
                while end <= (len(nums) - 1) and nums[end] == nums[index]:
                    end += 1
                return [start + 1, end - 1]
            else:
                if nums[index] > target:
                    return solve(left, index - 1)
                else:
                    return solve(index + 1, right)

        return solve(0, len(nums) - 1)
