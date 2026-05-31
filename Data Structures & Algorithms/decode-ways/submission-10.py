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

        # 2 6
        #[0,1,2]
        # if s[i-1] != "0":
        #     dp[i] = dp[i-1]
        # if i > 1:
        #     num = s[i-2:i]
        #     if '10' < num < '26':
        #         dp[i] = dp[i-2] + 2
          
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        def isValidSingleDigit(i):
            if s[i-1] != '0':
                return True
            return False

        def isValidDoubleDigit(i):
            if i-2 >= 0 and '10' <= s[i-2:i] <= '26':
                return True
            return False

        for i in range(1, n+1):
            num_add1 = dp[i-1] if isValidSingleDigit(i) else 0
            num_add2 = dp[i-2] if isValidDoubleDigit(i) else 0

            dp[i] = num_add1 + num_add2
        return dp[-1]
