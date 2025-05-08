from typing import List

# https://leetcode.com/problems/available-captures-for-rook


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        length = 8
        rook = (-1, -1)
        for y in range(length):
            for x in range(length):
                if board[y][x] == "R":
                    rook = (x, y)
                    break
        attacking = 0

        def check(x, y):
            nonlocal attacking
            nonlocal board
            cell = board[y][x]
            if cell == ".":
                return True
            if cell == "p":
                attacking += 1
            return False

        # right
        x = rook[0] + 1
        y = rook[1]
        while x < length:
            if check(x, y):
                x += 1
            else:
                break

        # left
        x = rook[0] - 1
        y = rook[1]
        while x >= 0:
            if check(x, y):
                x -= 1
            else:
                break

        # up
        x = rook[0]
        y = rook[1] - 1
        while y >= 0:
            if check(x, y):
                y -= 1
            else:
                break

        # down
        x = rook[0]
        y = rook[1] + 1
        while y < length:
            if check(x, y):
                y += 1
            else:
                break

        return attacking
