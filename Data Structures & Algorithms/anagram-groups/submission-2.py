from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = [0] * 26 # index 0-25
        global_counter = defaultdict(list)
        
        for string in strs: 
            # So we will have this count array for each str
            cur_cntr = alphabet.copy()
            for c in string:
                idx = ord(c) - 97
                cur_cntr[idx] += 1
            cur_cntr_t = tuple(cur_cntr)
            global_counter[cur_cntr_t].append(string)
        
        res = []
        for val in global_counter.values():
            res.append(val)

        return res