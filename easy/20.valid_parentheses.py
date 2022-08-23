"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid_test_1(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""
    
    def isValid_test_2(self, s: str) -> bool:
        stack = []
        dict = {"(":")", "[":"]", "{":"}"}
        for char in s:
            # If we have a left bracket, add it to the stack
            if char in dict:
                stack.append(char)
            # If the length of stack is 0, that means s started with )]} meaning invalid
            # Otherwise if the dict at the top item in stack is not equal to the current char, invalid (removes top from stack)
            elif not stack or dict[stack.pop()] != char:
                return False
        # After interating through all letters, not stack true means the stack has no values
        # no values mean each bracket has a corresponding close bracket
        return not stack
        
sol = Solution()
# s = "({}[])"
s = "(]"
ans = sol.isValid_test_2(s)
print(ans)


# Runtime: 50 ms, faster than 48.15% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 26.29% of Python3 online submissions for Valid Parentheses.
# Helped: Yes
