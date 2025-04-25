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

        def findFirst(left, right):
            debug("findFirst", left=left, right=right)
            if left > right:
                return -1

            index = (left + right) // 2
            if nums[index] == target:
                if index == 0:
                    return index
                if nums[index-1] < target:
                    return index

            if nums[index] >= target:
                return findFirst(left, index-1)
            else:
                return findFirst(index+1, right)

        def findLast(left, right):
            debug("findLast", left=left, right=right)
            if left > right:
                return -1

            index = (left + right) // 2
            if nums[index] == target:
                if index == len(nums)-1:
                    return index
                if nums[index+1] > target:
                    return index

            if nums[index] > target:
                return findLast(left, index-1)
            else:
                return findLast(index+1, right)

        return [
            findFirst(0, len(nums)-1),
            findLast(0, len(nums)-1)]


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
