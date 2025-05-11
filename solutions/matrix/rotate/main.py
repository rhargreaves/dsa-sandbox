from typing import List

# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix) - 1

        while left < right:
            top = left
            bottom = right

            for i in range(right - left):
                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft

            left += 1
            right -= 1
