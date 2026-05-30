class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
              a b a b d
            a 1 0
            b.  1 T 3 
            a.    1 0 
            b.      1 0
            d.        1
        '''

        # dp[i][j] means the if the s[i:j+1] substring could be a palindromic
        # true or false

        # 3,3
        # -> 
        # 2,4
        # ->
        # 1,5



        # state transfer function
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        dp = [[False] * len(s) for _ in range(len(s))]
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = True
                if j == i + 1 and s[j] == s[i]:
                    dp[i][j] = True

        start = 0
        max_len = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start+max_len]



        # # mid expand
        # def expand_odd(i):
        #     length = 0
        #     while i - length >= 0 and i + length < len(s) and s[i - length] == s[i + length]:
        #         length += 1
                
        #     length -= 1
        #     # inclusive
        #     return (i - length, i + length)
            
        # def expand_even(i, j):
        #     while i >= 0 and j < len(s) and s[i] == s[j]:
        #         i -= 1
        #         j += 1
            
        #     i += 1
        #     j -= 1
        #     return (i, j)
            
        # res = [0, 0]
        # for i in range(1, len(s)):
        #     x, y = expand_odd(i)
        #     j, k = expand_even(i-1, i)
        #     print(x, y)
        #     len1 = y - x + 1
        #     len2 = k - j + 1

        #     chosen_x = x
        #     chosen_y = y

        #     if len2 > len1:
        #         chosen_x = j
        #         chosen_y = k

        #     if (res[1] - res[0] + 1) < (chosen_y - chosen_x + 1):
        #         res[0] = chosen_x
        #         res[1] = chosen_y
        
        # return s[res[0]:res[1]+1]
            

                