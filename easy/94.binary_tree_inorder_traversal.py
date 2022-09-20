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
    # recursive solution
    def recursiveInorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    def iterativeInorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        cur = root

        # While current pointer is pointing somewhere or the stack has item(s) in it
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            # Now at leftmost node
            cur = stack.pop()
            res.append(cur.val)
            # Check if the node has right value
            cur = cur.right
        return res


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
rec_ans = sol.recursiveInorderTraversal(root)
print(rec_ans)

iter_ans = sol.iterativeInorderTraversal(root)
print(iter_ans)

#

#

# Time complexity:
