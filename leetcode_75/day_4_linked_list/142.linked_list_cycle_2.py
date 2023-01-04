from typing import Optional

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        # Wgile the head is not empty
        while head:
            # Add current node to set if not already in set
            if head not in seen:
                seen.add(head)
            # Else, the same object is already in set, means a loop has occurred, return the head
            else:
                return head
            # Increment the head to next node
            head = head.next
        # Return none is the loop finishes
        return None


# Runtime:
# Memory:
