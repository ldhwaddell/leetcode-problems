from typing import Optional

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use a recursive depth first search

        # Two empty trees are equal
        if not p and not q:
            return True

        # Above statment did not execute. Thi means that one
        # of the trees is null and the other is not, return False
        # OR if neither value is null but the value of the two
        # root nodes are not equal, return false.
        if not p or not q or p.val != q.val:
            return False

        # recursive step
        # if the values of the left and right nodes are equal, return true.
        # This recursively digs into the tree as long as there are nodes
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


sol = Solution()


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

ans = sol.isSameTree(root1, root2)
print(ans)


#

#

# Time complexity: O(p + q)
