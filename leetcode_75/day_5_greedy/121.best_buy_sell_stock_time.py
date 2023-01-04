"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):

            curr_profit = prices[r] - prices[l]

            if curr_profit > profit:
                profit = curr_profit

            if prices[r] < prices[l]:
                l = r
                r += 1

            else:
                r += 1

        return profit


sol = Solution()
# prices = [7, 1, 5, 3, 6, 4]
prices = [2, 1, 2, 1, 0, 1, 2]

ans = sol.maxProfit(prices)
print(ans)

# Runtime:

# Memory Usage:

# Time complexity:
