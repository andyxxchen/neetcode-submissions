'''
    dp[i][j] means if s1[:i] and s2[:j] can form s3[:i+j]
    abxycz
       "" x y z
    "" T  F F F
    a  F  
    b. F
    c. F

    s3[:i+j] could be from s1[:i] + s2[:j]
    dp[i][j] could be from dp[i-1][j] and s1[i-1] == s3[i+j-1] 
                        or dp[i][j-1] and s2[j-1] == s3[i+j-1]
    [[True, False, False, False, False], 
    [False, False, False, False, False], 
    [False, False, False, False, False], 
    [False, False, False, False, False], 
    [False, False, False, False, False]]

'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)


        if m + n != len(s3):
            return False
        
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True

                if j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
        
        print(dp)
        return dp[-1][-1]