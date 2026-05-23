from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for c in s:
            hashmap_s[c] += 1
        
        for c in t:
            hashmap_t[c] += 1

        return True if hashmap_s == hashmap_t else False