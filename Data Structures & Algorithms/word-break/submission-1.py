
'''
    "n e e t c o d e"
  [T F F F F F F F F] length of n + 1

    traverse s
        traverse wordDict
            if i-len(word) >= 0 and word matched and dp[i-len(word)] == T:
                True
    
    n = s.length
    m = avg(len of wordDict)
    r = len of wordDict

    O(m*n*r)
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n+1)
        print(dp)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                m = len(word)

                if i-len(word) >= 0 and s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True
                    
        
        return dp[-1]
