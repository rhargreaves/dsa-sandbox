from typing import List


# https://leetcode.com/problems/number-of-islands


class Solution:

    def __init__(self):
        self.parent = {}
        self.rank = {}  # track height of each tree
        self.count = 0

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.count += 1
            return self.parent[x]
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1
            self.count -= 1

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # Add current cell
                    self.find((r, c))

                    # Union with left
                    if c > 0 and grid[r][c - 1] == "1":
                        self.union((r, c), (r, c - 1))
                    # Union with up
                    if r > 0 and grid[r - 1][c] == "1":
                        self.union((r, c), (r - 1, c))
                    # Don't need to union right/down as we haven't processed these yet

        return self.count


class DfsBfsSolution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def walk(r, c):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"

            # left
            if c != 0:
                walk(r, c - 1)
            # right
            if c != cols - 1:
                walk(r, c + 1)
            # up
            if r != 0:
                walk(r - 1, c)
            # down
            if r != rows - 1:
                walk(r + 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    walk(r, c)

        return islands

    def numIslands_stack(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def walk(start_r, start_c):
            stack = []
            stack.append((start_r, start_c))
            while len(stack) != 0:
                r, c = stack.pop()

                if grid[r][c] == "0":
                    continue
                grid[r][c] = "0"

                # left
                if c != 0 and grid[r][c - 1] == "1":
                    stack.append((r, c - 1))
                # right
                if c != cols - 1 and grid[r][c + 1] == "1":
                    stack.append((r, c + 1))
                # up
                if r != 0 and grid[r - 1][c] == "1":
                    stack.append((r - 1, c))
                # down
                if r != rows - 1 and grid[r + 1][c] == "1":
                    stack.append((r + 1, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    walk(r, c)

        return islands
