import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        if len(piles) >= h: # need clarification here
            return upper_bound

        i = 1
        j = upper_bound
        res = upper_bound
        while i <= j and j>=1 and i <= upper_bound:
            m = i + (j-i) // 2
            if self.calc(piles, m) > h: # should increase the k to meet the requirement
                i = m + 1
            else:
                j = m - 1
                res = min(res, m)

        return res

    def calc(self, piles, k):
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        return total
        