class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j and i < len(nums) and j >= 0:
            m = i + (j-i) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                return m
        return -1