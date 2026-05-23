class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # probably want to have two arrays: one is the prefix product, and another is the suffix product.
        n = len(nums)
        # nums = [1,2,4,6]
        # prefix_prod = [1,1,2,8]

        prefix_prod = [1] * n

        for i in range(1,n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        res = []
        cur_prod = 1
        for i in range(n-1, -1, -1):
            res.append(prefix_prod[i] * cur_prod)
            cur_prod *= nums[i]

        return res[::-1]