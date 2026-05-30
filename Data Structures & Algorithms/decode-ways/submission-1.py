class Solution:
    def numDecodings(self, s: str) -> int:
        # 1 - 9
        # 10 - 26

        # 2 2 1
        # 1  

        #   1 + 1
        #   2

        # dp[i] means how many decode way ending with current i
        #  1  1. 1. 2
        # [0, 0, 0, 0]
        #    1 
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1] # add 1 digit
            # try add two
            if i >= 2:
                num = s[i-2:i]
                if '10' <= num <= '26':
                    dp[i] += dp[i-2]

        print(dp)
        return dp[-1]
