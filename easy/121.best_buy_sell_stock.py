"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 2 pointer method. Left pointer is index 0, right pointer is index 1
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            # Get profit by subtracting right from left
            curr_profit = prices[right] - prices[left]
            # If the current profit is greater than max profit, swap it
            if curr_profit > profit:
                profit = curr_profit

            # if the sell price is less than the current buy price,
            # make the buy the new sell price and increment the sell position
            if prices[right] < prices[left]:
                left = right
                right += 1
            # If the sell price is not less than the buy price, keep incrementing the sell pointer
            else:
                right += 1

        return profit


sol = Solution()
prices = [2, 1, 2, 1, 0, 1, 2]
ans = sol.maxProfit(prices)
print(ans)

#

#

# Time complexity:
