from typing import List

# https://leetcode.com/problems/friend-circles


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = {}
        count = n
        logs.sort(key=lambda log: log[0])

        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x
                count -= 1

        for timestamp, x, y in logs:
            union(x, y)
            if count == 1:
                return timestamp

        return -1
