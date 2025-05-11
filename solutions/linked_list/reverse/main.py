from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/reverse-linked-list/
# Key is to think about what the final state of each node
# should be after reversing


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    def reverseList_recur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def walk(node, prev):
            if node is None:
                return prev

            old_node = node.next
            node.next = prev
            return walk(old_node, node)

        return walk(head, None)
