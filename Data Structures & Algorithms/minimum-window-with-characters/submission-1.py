from collections import defaultdict


'''
    every time we add a new char 'A' in the window, we need to check if the 'A' can satisfy the need
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        need = len(count_t.keys()) # number of diff char we need
        have = 0
        freq_map = defaultdict(int)

        i = 0
        j = i

        def add(j):
            nonlocal have
            if s[j] in count_t:
                freq_map[s[j]] += 1
                if count_t[s[j]] == freq_map[s[j]]:
                    have += 1

        def remove(i):
            nonlocal have
            if s[i] in count_t:
                freq_map[s[i]] -= 1
                if count_t[s[i]] > freq_map[s[i]]:
                    have -= 1

        def isValid():
            nonlocal have, need
            return have == need
        
        res = (0, float('inf'))
        while j < len(s):
            add(j)
            # check if the window is valid?
            while i <= j and isValid():
                if j - i < res[1] - res[0]: # shorter valid found
                    res = (i, j)
                remove(i)
                i += 1
            j += 1
        
        if res[1] == float('inf'):
            return ""
        return s[res[0]:res[1]+1]
                


# from collections import defaultdict

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         str_map = defaultdict(int)
#         for c in t:
#             str_map[c] += 1
#         uniq_t = len(str_map.keys())
#         freq_map = defaultdict(int)

#         i = 0
#         j = i
#         def isValid(i, j):
#             for c in str_map:
#                 if freq_map[c] < str_map[c]:
#                     return False            
#             return True
        
#         res = (0, float('inf'))
#         while j < len(s):
#             freq_map[s[j]] += 1
#             # check if the window is valid?
#             while i <= j and isValid(i, j):
#                 if j - i < res[1] - res[0]: # shorter valid found
#                     res = (i, j)
#                 freq_map[s[i]] -= 1
#                 i += 1
#             j += 1
        
#         if res[1] == float('inf'):
#             return ""
#         return s[res[0]:res[1]+1]
                