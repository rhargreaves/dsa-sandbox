from collections import defaultdict
from typing import List

# https://leetcode.com/problems/number-of-equivalent-domino-pairs


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        def key(pair):
            if pair[0] < pair[1]:
                return (pair[0], pair[1])
            else:
                return (pair[1], pair[0])

        seen = defaultdict(lambda: 0)
        pairs = 0
        for pair in dominoes:
            if key(pair) in seen:
                seen[key(pair)] += 1
                pairs += seen[key(pair)]
            else:
                seen[key(pair)] = 0
        return pairs
