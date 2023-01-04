from typing import Optional

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        # If there is no root, return nothing
        if not root:
            return []

        # Create a queue
        queue = [root]
        output = []

        while queue:
            current_vals = []
            for _ in range(len(queue)):
                curr_node = queue.pop(0)
                current_vals.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            output.append(current_vals)

        return output


# Runtime:

# Memory Usage:

# Time complexity:
