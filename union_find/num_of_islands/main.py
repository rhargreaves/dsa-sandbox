from typing import List


# https://leetcode.com/problems/number-of-islands


class Solution:
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
