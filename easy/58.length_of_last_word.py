"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord_v1(self, s: str) -> int:
        return 0 if len(s) == 0 else len(s.strip().split(" ")[-1])

    def lengthOfLastWord_v2(self, s: str) -> int:
        # Last item in s
        i = len(s) - 1
        # length of string
        length = 0

        while s[i] == " ":
            # starts at end, while the characters are spaces, decrement i
            i -= 1
        while i >= 0 and s[i] != " ":
            i -= 1
            length += 1
        return length


sol = Solution()
s = "   fly me   to   the moon  "
ans = sol.lengthOfLastWord_v1(s)
print(ans)

ans = sol.lengthOfLastWord_v2(s)
print(ans)
# Runtime: 59 ms, faster than 17.32% of Python3 online submissions for Length of Last Word.

# Memory Usage: 14 MB, less than 5.76% of Python3 online submissions for Length of Last Word.

# Time complexity:
