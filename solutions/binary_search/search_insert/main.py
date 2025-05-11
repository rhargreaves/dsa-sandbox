from typing import List


# nums is sorted in ascending order and contains distinct values
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def find(left, right):
            if left > right:
                return left

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                return find(left, mid - 1)
            else:
                return find(mid + 1, right)

        return find(0, len(nums) - 1)
