"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if len(s) == 0 else len(s.strip().split(" ")[-1])


sol = Solution()
s = "   fly me   to   the moon  "
ans = sol.lengthOfLastWord(s)
print(ans)

# Runtime: 59 ms, faster than 17.32% of Python3 online submissions for Length of Last Word.

# Memory Usage: 14 MB, less than 5.76% of Python3 online submissions for Length of Last Word.

# Time complexity:
