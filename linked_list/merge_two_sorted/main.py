from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_node = list1
        l2_node = list2
        dummy = ListNode()
        node = dummy
        while l1_node or l2_node:
            if (l1_node and l2_node and l1_node.val < l2_node.val) or (
                l1_node and not l2_node
            ):
                node.next = ListNode(l1_node.val)
                l1_node = l1_node.next
            elif l2_node:
                node.next = ListNode(l2_node.val)
                l2_node = l2_node.next

            node = node.next

        return dummy.next
