class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def back_tracking(start, path, summ):
            if summ == target:
                res.append(path[:])
            
            if summ > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                back_tracking(i, path[:], summ+nums[i])
                path.pop()
            
            return

        back_tracking(0, [], 0)
        return res

