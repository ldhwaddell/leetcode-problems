"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list[int]:
        s = []

        def depth_first_search(root):
            # If there is no root, break from recursing function
            if not root:
                return
            # Append the root node val to s
            s.append(root.val)
            # If there are multiple children call dfs on each child
            for child in root.children:
                depth_first_search(child)

        depth_first_search(root)
        return s


# Runtime:

# Memory Usage:

# Time complexity:
