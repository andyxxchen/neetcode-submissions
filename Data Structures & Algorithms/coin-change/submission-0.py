
'''
    2 = 1 + 6


    1, 5, 6 -> 7
     0             7
    [0,1,2,3,4,1,1,2]
    dp[0] = 0
    0 -> 12 traverse
        for each coin check if i-coin >= 0
            dp[i] = min(dp[i], dp[i-coin] + 1)
    

'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
