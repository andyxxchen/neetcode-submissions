from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to record index as value
        hashmap = defaultdict(int)

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                result = [hashmap[complement], i]
                result.sort()
                return result
            hashmap[nums[i]] = i
        
        
        return [-1,-1]