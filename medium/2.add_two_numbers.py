from typing import Optional

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""


class Node:
    def __init__(self, val=0, next=None):
        """Initialize a single node"""
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        """Initialize head of list, pointing nowhere"""
        # All the linked list needs is a head to initialize
        self.head = None

    def add(self, new_val):
        """Add a value to the linked list"""
        # Get the value from params
        new_node = Node(new_val)

        # If the list is empty, meaning head points nowhere
        # Make the head of the list the new node
        if self.head is None:
            self.head = new_node
            return

        # Else list does have a head
        # Start the cursor at the head of the list
        cursor = self.head
        # While the cursor does have a next value
        while cursor.next:
            # iterate over the nodes
            # The cursor is pointed to the next node until there is no next node
            cursor = cursor.next
        # Once there is no longer a next node,
        # the cursor (last item in list at this point)
        # gets pointed to the newly created node
        cursor.next = new_node

    def print_linked_list(self):
        """Output each value"""
        vals = []
        # If the linked list doesnt have a head, return nothing
        if self.head is None:
            return ""
        # Else, linked list does have a head. Make the start node the head of the list (item one)
        start_node = self.head
        # While there is a start node
        while start_node:
            # Print the nodes value
            # print(start_node.val, end=" ")
            vals.append(start_node.val)
            # Point the start node to the next node
            start_node = start_node.next
        return vals


class Solution:
    def addTwoNumbers(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        while l1 or l2:
            print(l1)
            print(l2)
        return l1


list1 = LinkedList()
list2 = LinkedList()

list1.add(2)
list1.add(4)
list1.add(3)

list2.add(5)
list2.add(6)
list2.add(4)

print(f"list1: {list1.print_linked_list()}")
print(f"list2: {list2.print_linked_list()}")
sol = Solution()
ans = LinkedList()
ans = sol.addTwoNumbers(list1, list2)
print(ans.print_linked_list())
