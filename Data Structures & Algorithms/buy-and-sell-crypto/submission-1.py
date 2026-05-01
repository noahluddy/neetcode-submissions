# Dynamic Programming

# O(n) T, O(1) S

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for sell in prices:
            max_profit = max(max_profit, sell - min_price)
            min_price = min(min_price, sell)

        return max_profit