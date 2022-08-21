"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:

        prefix = ""
        start = ""
        for i in range(len(strs[0])):
            start += strs[0][i]
            for word in strs:
                if word.startswith(start):
                    prefix = start
                else:
                    prefix = start[:-1]
                    break
            else:
                continue
            break

        return prefix


sol = Solution()
strs = ["flower", "flow", "flight"]
ans = sol.longest_common_prefix(strs)
print(ans)

# Runtime: 38 ms, faster than 89.31% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 50.32% of Python3 online submissions for Longest Common Prefix.
