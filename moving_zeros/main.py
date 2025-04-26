from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        num = 0
        while r < len(nums):
            num = nums[r]
            r += 1

            if num != 0:
                nums[w] = num
                num = 0
                w += 1

        while w < len(nums):
            nums[w] = 0
            w += 1

    def moveZeroes_naive(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        moved = True
        while moved:
            moved = False
            for i in range(len(nums)):
                if nums[i] == 0 and i != len(nums) - 1 and nums[i + 1] != 0:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    moved = True
                elif (
                    nums[i] == 0
                    and i <= len(nums) - 4
                    and nums[i + 1] == 0
                    and nums[i + 2] != 0
                    and nums[i + 3] != 0
                ):
                    nums[i], nums[i + 1], nums[i + 2], nums[i + 3] = (
                        nums[i + 2],
                        nums[i + 3],
                        nums[i],
                        nums[i + 1],
                    )
                    moved = True
