from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0  # track max diameter globally

        def height(node):  # track height with recursion
            nonlocal max_diameter

            if not node:
                return -1  # key to this problem

            lh = height(node.left) + 1
            rh = height(node.right) + 1

            diameter = lh + rh
            max_diameter = max(diameter, max_diameter)
            return max(lh, rh)

        height(root)
        return max_diameter
