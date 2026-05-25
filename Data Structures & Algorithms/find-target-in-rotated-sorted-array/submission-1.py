# find which part is the desired ordered part

# [3,4,5,6,1,2] left ordered , in ordered? -> Yes, go to ordered, no -> go to the other side
# [1,2,3,4,5,6] left ordered 
# [5,6,1,2,3,4] right ordered 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        def isInRange(a, b):
            nonlocal target
            if nums[a] <= target <= nums[b]:
                return True
            return False
        res = -1
        while i < j:
            m = i + (j - i) // 2
            
            if nums[i] <= nums[m]:
                # left ordered
                if isInRange(i, m):
                    j = m
                else:
                    i = m + 1
            else: 
                # right ordered
                if isInRange(m, j):
                    i = m
                else:
                    j = m - 1

        if nums[i] == nums[j] == target:
            res = i
        return res

