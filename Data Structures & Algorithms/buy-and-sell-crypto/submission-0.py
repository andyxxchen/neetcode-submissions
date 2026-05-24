class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        # sliding window
        i = 0
        j = i+1
        while j < len(prices):
            res = max(res, prices[j]-prices[i])
            if prices[j] < prices[i]:
                # move i to the j
                i = j
            j += 1

        return res