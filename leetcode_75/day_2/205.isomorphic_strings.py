"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped_chars = ""
        if len(set(s)) != len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]

            mapped_chars += mapping[s[i]]

        return t == mapped_chars


sol = Solution()
s = "badc"
t = "baba"
ans = sol.isIsomorphic(s, t)
print(ans)

#

#

# Time complexity:
