
# n = len(nums)
# the largest summy of all the subarrary ending with nums[i] (inclusive)

# transfer formula -> dp[i] = max[nums[i], dp[i-1] + nums[i]]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        
        for i in range(n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            
        return max(dp)