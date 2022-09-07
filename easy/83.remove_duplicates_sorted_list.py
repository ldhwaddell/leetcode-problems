"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        """Initialize a single node"""
        self.val = val
        self.next = next


class Solution:
    pass


sol = Solution()
n = 2
ans = sol.climbStairs(n)
print(ans)

# Runtime: 55 ms, faster than 26.27% of Python3 online submissions for Climbing Stairs.

# Memory Usage: 13.9 MB, less than 11.83% of Python3 online submissions for Climbing Stairs.

# Time complexity:
