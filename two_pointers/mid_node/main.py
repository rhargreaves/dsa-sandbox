# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        half_node = head
        i = 0
        while cur_node:
            cur_node = cur_node.next
            i += 1
            i %= 2
            if i == 0:
                half_node = half_node.next

        return half_node

    def middleNode_naive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        mid = (len(nodes) - 1) // 2
        if len(nodes) % 2 == 0:
            return nodes[mid + 1]
        else:
            return nodes[mid]
