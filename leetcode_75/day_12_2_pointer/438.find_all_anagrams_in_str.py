from typing import List
from collections import Counter
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count, s_count = {}, {}

        # Create hashmap with all chars in p 


        



        print(p_count, s_count, p_count==s_count)





sol = Solution()
s = "ababababab" 
p = "aab"
ans = sol.findAnagrams(s, p)
print(ans)

#

#

# Time complexity:
