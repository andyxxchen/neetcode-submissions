class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] == True:
                    res += 1

        return res

        '''
            [[True, True, True, False, False], 
            [False, True, True, True, False], 
            [False, False, True, True, True], 
            [False, False, False, True, True], 
            [False, False, False, False, True]]

        '''


        # def expand(i):
        #     length = 0
        #     while i - length >= 0 and i + length < len(s):
        #         if s[i - length] != s[i + length]:
        #             break
        #         length += 1
        #     return length

    
        # def expand_even(j):
        #     length = 0
        #     i = j-1
        #     while i-length >= 0 and j+length < len(s):
        #         if s[i-length] != s[j+length]:
        #             break
        #         length += 1
        #     return length

        # res = 1
        # for i in range(1, len(s)):
        #     res += expand(i)
        #     res += expand_even(i)
        
        # return res
