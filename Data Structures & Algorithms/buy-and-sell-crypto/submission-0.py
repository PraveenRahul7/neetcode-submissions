class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        buy = float('inf')
        for price in prices: 
            buy = min(buy, price)
            profit = price-buy
            res = max(res, profit)
        return res
        
        