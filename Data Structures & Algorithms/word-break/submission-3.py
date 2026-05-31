
'''.         4     6
             i     j
    "n e e t c o d e"
  [T F F F T F F F F] length of n + 1
   0 1 2 3 4 5
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
        dp[0] = True

        for j in range(n):
            for i in range(j+1):
                cur_word = s[i:j+1]
                if cur_word in wordDict:
                    if dp[i]:
                        dp[j+1] = True

        print(dp)
        return dp[-1]
