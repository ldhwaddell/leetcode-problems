"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean string by converting all chars to lower case and
        # removing any non alphanumeric characters

        s_cleaned = [i.lower() for i in s if i.isalnum()]

        return s_cleaned == s_cleaned[::-1]


sol = Solution()
s = "race a car"
ans = sol.isPalindrome(s)
print(ans)

#

#

# Time complexity:
