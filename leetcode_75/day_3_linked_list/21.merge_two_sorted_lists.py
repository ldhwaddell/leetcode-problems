"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # cursor anddummy point to the same spot in memory. So we can manipulate the cursor and the dummy will still be the start
        dummy = ListNode()
        cursor = dummy
        # While neither list is empty. When we set list = list.next, if list.next is None it will exit loop
        while list1 and list2:
            # If list 1 value is less than that of list 2 set the cursors next item to be list 1.
            # Update list1 to be the next node in list
            if list1.val < list2.val:
                # Point cursor to the head
                cursor.next = list1
                # update list 1
                list1 = list1.next
            # Else list2 value is greater than or equal to list1 value
            else:
                # Point the cursor to head of list 2
                cursor.next = list2
                # update list 2
                list2 = list2.next
            # Update cursor after each merge operation
            cursor = cursor.next

        # After merging, if list1 still has a value, set the cursors next to list1
        if list1:
            cursor.next = list1
        # Otherwise, set the cursors next to list2
        if list2:
            cursor.next = list2

        return dummy.next


# Runtime:
# Memory:
