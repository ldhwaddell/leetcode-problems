from typing import Optional

"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        """Initialize a single node"""
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current node is head of list
        cur = head
        # while the current node has not been pointed to none
        while cur:
            # while the current node has a next value and the next nodes value equals the current nodes value
            while cur.next and cur.next.val == cur.val:
                # skip over it by assigning the next node to be the one after next
                cur.next = cur.next.next
            # other wise, advance the current node
            cur = cur.next
        # return the list
        return head


sol = Solution()
ans = sol.deleteDuplicates()
print(ans)

# Runtime: 77 ms, faster than 30.77% of Python3 online submissions for Remove Duplicates from Sorted List.

# Memory Usage: 14 MB, less than 30.02% of Python3 online submissions for Remove Duplicates from Sorted List.

# Time complexity:
