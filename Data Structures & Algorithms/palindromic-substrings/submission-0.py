class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i):
            length = 0
            while i - length >= 0 and i + length < len(s):
                if s[i - length] != s[i + length]:
                    break
                length += 1
            return length

    
        def expand_even(j):
            length = 0
            i = j-1
            while i-length >= 0 and j+length < len(s):
                if s[i-length] != s[j+length]:
                    break
                length += 1
            return length

        res = 1
        for i in range(1, len(s)):
            res += expand(i)
            res += expand_even(i)
        
        return res
