from typing import Optional

"""
Given the root of a binary tree, return the inorder traversal of its Nodes' values.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # create the empty stack data structure
        stack = []
        # set pointer node to the root
        ptr = root

        while True:
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                break
        
        
        print([i.val for i in stack])




sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol.inorderTraversal(root)

#

#

# Time complexity:
