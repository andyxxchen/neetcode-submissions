from collections import defaultdict

class Solution:

    '''

        most_freq_char = 'A' 
        freq_map = {}
        the current most frequent char in the sliding window
         j
        "AAABABB"

        "AABBBBC" k = 2 -> 6

        A = 2
        B = 2
        most_freq_char = A 
        update freq_map
        update freq_char

        see if it's valid window? k > 0? 

        if yes
            move j to the next one
            end the loop
        if not 
            shrink the window, until valid
                i += 1
    
        at the end of every loop we make sure the window is valid
    '''



    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        freq_char = s[0]

        def isValid(i, j, k):
            length = j - i + 1
            if length - freq_map[freq_char] <= k:
                return True
            return False
        
        i = 0
        j = i
        res = 0
        while j < len(s):
            # update freq_map and freq_char
            freq_map[s[j]] += 1
            if freq_map[s[j]] > freq_map[freq_char]:
                freq_char = s[j]

            # is it a valid window? 
            if not isValid(i, j, k):
                # shirnk the window
                freq_map[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res

        


        