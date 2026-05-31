
'''

    [1,2,-3,4]
    [1,2,-3,4]
    [1,2,-6,-24]

    2 x n dp array, max/min prod ending with nums[i]

    0 -> reset dp[0][i] and dp[1][i]

    nums[i] > 0 
            -> dp[0][i] = max(dp[0][i-1] * nums[i], nums[i])
            -> dp[1][i] = min(dp[1][i-1] * nums[i], nums[i])

    nums[i] < 0 
        -> dp[0][i] = max(dp[1][i-1] * nums[i], nums[i])
        -> dp[1][i] = min(dp[0][i-1] * nums[i], nums[i])

    max [ ]
    min [ ]
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[1] * n for _ in range(2)]

        for i in range(n):
            if nums[i] > 0:
                dp[0][i] = max(dp[0][i-1] * nums[i], nums[i])
                dp[1][i] = min(dp[1][i-1] * nums[i], nums[i])
            elif nums[i] < 0:
                dp[0][i] = max(dp[1][i-1] * nums[i], nums[i])
                dp[1][i] = min(dp[0][i-1] * nums[i], nums[i])
            else:
                dp[0][i] = dp[1][i] = 0


        return max(dp[0])

