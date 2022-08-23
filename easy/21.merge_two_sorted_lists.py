from typing import Optional

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

# Definition for singly-linked list.
class Node:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
      printval = self.head
      while printval is not None:
         print (printval.val)
         printval = printval.next


class Solution:
    def mergeTwoLists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        # Make the dummy and cursor both point to first item in list
        # Both nodes with current value of zero and next pointed to nowhere
        dummy = cursor = Node(0)

        # Ensure neither list is empty
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
        cursor.next = list1 or list2 
        return dummy.next


def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = Node(val, head)
    return head

def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

