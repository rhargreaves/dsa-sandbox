from collections import defaultdict
from typing import List


# Union Find solution
# Complexity: O(e * a(n)) time
class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):  # path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def find_slow(x):  # without path compression
            if parent[x] == x:
                return x
            else:
                return find(parent[x])

        def union(x, y):
            r1 = find(x)
            r2 = find(y)

            if r1 == r2:
                return

            if rank[r2] > rank[r1]:
                r1, r2 = r2, r1
            parent[r2] = r1

            if rank[r1] == rank[r2]:
                rank[r2] += 1

        for edge in edges:
            union(edge[0], edge[1])

        return find(source) == find(destination)


# Graph solution (not as efficient as Union Find)
# Complexity: O(n + e) time, O(n + e) space
class Solution_Graph:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        visited = set()

        next_nodes = defaultdict(lambda: [])

        for edge in edges:
            next_nodes[edge[0]].append(edge[1])
            next_nodes[edge[1]].append(edge[0])

        def solve(cur_node):
            if cur_node in visited:
                return False

            visited.add(cur_node)

            if cur_node == destination:
                return True

            for next in next_nodes[cur_node]:
                if solve(next):
                    return True

            return False

        return solve(source)
