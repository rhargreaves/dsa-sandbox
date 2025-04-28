from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
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
