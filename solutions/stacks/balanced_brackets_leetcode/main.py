# see https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ["(", "[", "{"]
        closings = [")", "]", "}"]

        for c in s:
            if c in openings:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                opener = stack.pop()
                o_index = openings.index(opener)
                expected_closer = closings[o_index]
                if expected_closer != c:
                    return False

        return len(stack) == 0
