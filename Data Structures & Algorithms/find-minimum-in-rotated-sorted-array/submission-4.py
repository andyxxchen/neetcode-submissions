

#  i   m     j 
# [3,4,5,6,1,2]. b r
# [6,1,2,3,4,5]  s l
# [5,6,1,2,3,4]. s l include
# [4,5,6,1,2,3]  b r

# 1 2 3 s l
# 3 1 2 s l include
# 2 3 1 b r
# 1 2   s l include
# 2 1.  b r



# if m >= i, right or m res = min(nums[i], res)
# if m < i, left
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if l == r:
            return nums[0]

        res = float('inf')
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m
        
        if l == r:
            res = min(res, nums[l + (r - l) // 2])
        return res