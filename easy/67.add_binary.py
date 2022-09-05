"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

        # reverse input strings
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = digit_a + digit_b + carry
            char = str(total % 2)
            result = char + result
            carry = total // 2

        if carry:
            result = "1" + result
        
        return result

sol = Solution()
a = "1010"
b = "1011"
ans = sol.addBinary(a, b)
print(ans)


# 

# 

# Time complexity:
