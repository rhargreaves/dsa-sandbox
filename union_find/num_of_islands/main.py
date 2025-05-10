from typing import List


# https://leetcode.com/problems/number-of-islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def walk(r, c):
            if grid[r][c] == "0":
                return
            if (r, c) in visited:
                return
            visited.add((r, c))

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
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    walk(r, c)

        return islands
