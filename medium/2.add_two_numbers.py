from typing import Optional

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        """Initialize a single node"""
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # initialize a current node to the dummy head of the list to be returned
        dummy_head = cur = ListNode(0)
        # Set the carry value to 0
        carry = 0

        # Do operation while l1 has a node, l2 has a node, or the carry flag is not 0
        while l1 or l2 or carry:
            # only get an x or y val if there exists a node in the respective list
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Sum the nodes and carry flag (flag starts at 0)
            sum = x + y + carry
            # Make the carry flag the ones digit of sum (8 + 7 = 15 -> 15 // 10 = 1)
            carry = sum // 10
            # make the sum just the units of sum as if the sum has made carry > 0, it will be added to the next node
            sum = sum % 10
            # make the cur node point to the new value
            cur.next = ListNode(sum)
            # Advance current node to next (newly created node)
            cur = cur.next
            # advance l1 and l2 if the have next values
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the values the dummy head points to
        return dummy_head.next


# Runtime: 69 ms, faster than 94.09% of Python3 online submissions for Add Two Numbers.

# Memory Usage: 13.8 MB, less than 99.26% of Python3 online submissions for Add Two Numbers.
