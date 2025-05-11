from typing import List

# https://leetcode.com/problems/number-of-equivalent-domino-pairs


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = {}
        pairs = 0
        for pair in dominoes:
            key = tuple(sorted(pair))

            if key in seen:
                seen[key] += 1
                pairs += seen[key]
            else:
                seen[key] = 0
        return pairs
