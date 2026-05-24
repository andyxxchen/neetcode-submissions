class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        res = 0
        for num in nums:
            cur = 0
            while num + cur in num_set:
                cur += 1

            res = max(res, cur)

        return res