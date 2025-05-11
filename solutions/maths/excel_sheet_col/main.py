# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = columnNumber
        letters = []
        while a != 0:
            a -= 1  # key!
            letter = chr(ord("A") + (a % 26))
            letters.insert(0, letter)
            a //= 26
        return "".join(letters)
