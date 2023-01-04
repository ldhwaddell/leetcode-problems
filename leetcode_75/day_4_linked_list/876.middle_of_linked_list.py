from typing import Optional

"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr

        


# Runtime:
# Memory:
