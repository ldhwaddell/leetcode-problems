"""
Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

        # reverse input strings
        a, b = a[::-1], b[::-1]

        # Iterate through longest string amount of times
        for i in range(max(len(a), len(b))):
            # only assign digits if i is less than the last index of list
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            # Sum the digits and carry
            total = digit_a + digit_b + carry
            char = str(total % 2)
            # Add the digit to result string
            result = char + result
            # only have a carry if total is 2 or 3. if 1, carry is 0
            carry = total // 2

        # Add end of loop if carry flag has value, add a one to result string
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
