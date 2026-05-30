class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [[0] * len(nums) for _ in range(2)]
        
        # rob 0 
        dp[0][0] = nums[0]
        dp[0][1] = max(dp[0][0], nums[1])
        # not rob 0
        dp[1][0] = 0
        dp[1][1] = nums[1]

        for i in range(2, len(nums)):
            dp[0][i] = max(dp[0][i-1], dp[0][i-2] + nums[i])
            dp[1][i] = max(dp[1][i-1], dp[1][i-2] + nums[i])

        return max(dp[0][-2], dp[1][-1])