from typing import Optional

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min=float("-inf"), max=float("inf")):
            # If there is no root, break from recursing function and return true
            if not root:
                return True

            # Check conditions
            if root.val <= min or root.val >= max:
                return False

            print(root.val, min)
            print(root.val, max)

            return validate(root.left, min, root.val) and validate(
                root.right, root.val, max
            )

        return validate(root)


# Runtime:

# Memory Usage:

# Time complexity: