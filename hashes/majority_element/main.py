from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = defaultdict(lambda: 0)
        top_freq = 0
        top_element = None
        for n in nums:
            freqs[n] += 1
            if freqs[n] > top_freq:
                top_freq = freqs[n]
                top_element = n
            if top_freq > len(nums) // 2:
                break
        return top_element
