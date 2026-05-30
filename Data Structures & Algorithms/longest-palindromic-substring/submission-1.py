class Solution:
    def longestPalindrome(self, s: str) -> str:
        # mid expand

        def expand_odd(i):
            length = 0
            while i - length >= 0 and i + length < len(s) and s[i - length] == s[i + length]:
                length += 1
                
            length -= 1
            # inclusive
            return (i - length, i + length)
            
        def expand_even(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            i += 1
            j -= 1
            return (i, j)
            
        res = [0, 0]
        for i in range(1, len(s)):
            x, y = expand_odd(i)
            j, k = expand_even(i-1, i)
            print(x, y)
            len1 = y - x + 1
            len2 = k - j + 1

            chosen_x = x
            chosen_y = y

            if len2 > len1:
                chosen_x = j
                chosen_y = k

            if (res[1] - res[0] + 1) < (chosen_y - chosen_x + 1):
                res[0] = chosen_x
                res[1] = chosen_y
        
        return s[res[0]:res[1]+1]
            

                