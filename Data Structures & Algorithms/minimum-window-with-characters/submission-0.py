from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        str_map = defaultdict(int)
        for c in t:
            str_map[c] += 1
        uniq_t = len(str_map.keys())
        freq_map = defaultdict(int)

        i = 0
        j = i
        def isValid(i, j):
            for c in str_map:
                if freq_map[c] < str_map[c]:
                    return False            
            return True
        
        res = (0, float('inf'))
        while j < len(s):
            freq_map[s[j]] += 1
            # check if the window is valid?
            while i <= j and isValid(i, j):
                if j - i < res[1] - res[0]: # shorter valid found
                    res = (i, j)
                freq_map[s[i]] -= 1
                i += 1
            j += 1
        
        if res[1] == float('inf'):
            return ""
        return s[res[0]:res[1]+1]
                