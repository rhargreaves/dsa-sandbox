from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqs = defaultdict(lambda: 0)
        for n in arr:
            freqs[n] += 1
        return len(freqs.keys()) == len(set(freqs.values()))
