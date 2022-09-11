"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[0] = nums2[0] if m == 0 and n == 1 else nums1[0]
        if m and n:
            nums2_pointer = 0
            for i in range(n):
                if nums1[i] < nums2[i]:
                    nums1.insert(i + 1, nums2[i])

        print(nums1)


sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 1
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)

#

#

# Time complexity:
