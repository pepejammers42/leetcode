# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # only care about the "net positives"
        
        prof = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                prof += prices[i] - prices[i-1]
        return prof
