from typing import List


class Solution:
    # O(n) time, O(1) space (nice math trick)
    def missingNumber(self, nums: List[int]) -> int:
        expected_total = sum([i for i in range(len(nums) + 1)])
        actual_total = sum(nums)
        return expected_total - actual_total

    # O(n) time, O(n) space
    def missingNumber_naive(self, nums: List[int]) -> int:
        num_set = set(nums)
        for n in num_set:
            if n != 0 and n - 1 not in num_set:
                return n - 1
            if n + 1 not in num_set:
                return n + 1
