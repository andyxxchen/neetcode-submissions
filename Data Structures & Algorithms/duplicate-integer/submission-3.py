from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i, num in enumerate(nums):
            if num in hashset:
                return True
            hashset.add(num)
        return False