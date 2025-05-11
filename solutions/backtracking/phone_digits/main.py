from typing import List


# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        stack = []
        combinations = []
        if len(digits) == 0:
            return combinations

        def backtrack(i):
            nonlocal stack

            if i >= len(digits):
                combinations.append("".join(stack))
                return

            for letter in letters[digits[i]]:
                stack.append(letter)
                backtrack(i + 1)
                stack.pop()

        backtrack(0)
        return combinations


class Solution_ImplicitBacktracking:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        combinations = []
        if len(digits) == 0:
            return []

        def backtrack(i, current):
            if i >= len(digits):
                combinations.append(current)
                return

            for letter in letters[digits[i]]:
                backtrack(i + 1, current + letter)

        backtrack(0, "")
        return combinations
