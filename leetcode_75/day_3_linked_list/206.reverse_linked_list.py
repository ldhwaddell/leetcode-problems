from typing import Optional

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set current pointer to the head
        curr = head
        # Set the previous pointer to none
        prev = None

        # While the current pointer is not none
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


# Runtime:
# Memory:
