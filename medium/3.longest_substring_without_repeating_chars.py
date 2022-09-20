"""
Given a string s, find the length of the longest substring without repeating cacters.

"sliding window"

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        used = {}

        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            used[c] = i
        return max_length


sol = Solution()
s = "pwwkew"
ans = sol.lengthOfLongestSubstring(s)
print(ans)


#

#

# Time complexity:
