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
        anagrams = []
        remove = 0

        # Create hashmap with all chars in p
        for c in p:
            if c not in p_count:
                p_count[c] = 1
            else:
                p_count[c] += 1

        print(f"p count: {p_count}")

        s_count[s[0]] = 1
        s_count[s[1]] = 1 if s[0] != s[1] else 2

        for i in range(2, len(s)):
            # Add new letter to dict
            if s[i] not in s_count:
                s_count[s[i]] = 1
            else:
                s_count[s[i]] += 1

            print(s_count)


            # Check for dict equality
            if s_count == p_count:
                anagrams.append(remove)

            

            s_count[s[remove]] -= 1

            remove += 1
        return anagrams


sol = Solution()
s = "abab"
p = "ab"
ans = sol.findAnagrams(s, p)
print(ans)

#

#

# Time complexity:
