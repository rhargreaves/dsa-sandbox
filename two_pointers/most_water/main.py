from typing import List

# https://leetcode.com/problems/container-with-most-water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while j > i:
            lowest_height = min(height[i], height[j])
            area = lowest_height * (j - i)
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


# always move the pointer of the lower height inwards
# this is because the area is limited by the lower height
# so we need to move the pointer of the lower height inwards
# to find a higher height
