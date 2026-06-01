'''
    dp[i][j] means the longest common subsequence between text1[:i+1] and text2[:j+1]
    
    
    
      c a t 
    c 1 1 1
    r 1 1 1
    a 1 
    b 1
    t 1

    [[1, 1, 1], 
     [1, 0, 0], 
     [1, 2, 0], 
     [1, 0, 0], 
     [1, 0, 1]]

      y b y
    b 0 1 1
    l 0 1 1

    [[0, 1, 1], 
     [0, 1, 1]]

    if text1[i] == text2[j]:
        max()

'''



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in range(len(text1))]

        for j in range(len(text2)):
            if text1[0] == text2[j]:
                dp[0][j] = 1
                continue
            dp[0][j] = dp[0][j-1]
            
        for i in range(len(text1)):
            if text2[0] == text1[i]:
                dp[i][0] = 1
                continue
            dp[i][0] = dp[i-1][0]


        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]
        



