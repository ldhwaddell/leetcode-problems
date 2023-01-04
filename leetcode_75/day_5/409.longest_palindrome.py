"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c]+=1
        print(dic)
        return "piss"
        


sol = Solution()
s = "abccccdd"
ans = sol.longestPalindrome(s)
print(ans)

# Runtime:

# Memory Usage:

# Time complexity:
