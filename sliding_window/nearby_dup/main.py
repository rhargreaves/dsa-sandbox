from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pool = set()
        if k == 0:
            return False

        for i in range(len(nums)):
            if nums[i] in pool:
                return True
            pool.add(nums[i])
            if i >= k:
                pool.remove(nums[i - k])

        return False

    def containsNearbyDuplicate_naive(self, nums: List[int], k: int) -> bool:
        pool = set()
        if k == 0:
            return False

        j = 0
        for i in range(len(nums)):
            if nums[i] in pool:
                return True
            if i - j < k:
                pool.add(nums[i])
            else:
                pool.remove(nums[j])
                pool.add(nums[i])
                j += 1

        return False
