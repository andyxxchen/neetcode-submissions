class Solution:
    '''

    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()

        res = 0

        i = 0
        j = i
        while j < len(s):
            # in hashset, shrink window, until not
            while s[j] in hashset:
                hashset.remove(s[i])
                i += 1
            # until it's not in hashset, start expanding 
            hashset.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res