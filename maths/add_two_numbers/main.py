from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def buildNumber(node, multiplier):
            if node.next is None:
                return node.val * multiplier
            return buildNumber(node.next, multiplier * 10) + (node.val * multiplier)

        a = buildNumber(l1, 1)
        b = buildNumber(l2, 1)

        result = a + b

        root = ListNode()
        node = root
        digits = [int(n) for n in str(result)]
        node.val = digits.pop()
        while len(digits) != 0:
            node.next = ListNode()
            node = node.next
            node.val = digits.pop()
        return root
