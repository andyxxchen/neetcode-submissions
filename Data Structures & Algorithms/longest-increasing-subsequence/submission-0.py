'''
    dp[i] means the length of the longest subsequence ending with nums[i]
    [1,1,1,1,1,1,1]
       j
    [9,1,4,2,3,3,7]

    traverse nums
        traverse i from 0 to j
            if num[j] > num[i]:
                dp[j] = max(dp[j], dp[i] + 1)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)