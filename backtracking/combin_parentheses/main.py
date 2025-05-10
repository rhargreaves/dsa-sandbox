from typing import List

# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base case: open == closed == n
        # can open if open < n:
        # can close if closed < open

        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res
