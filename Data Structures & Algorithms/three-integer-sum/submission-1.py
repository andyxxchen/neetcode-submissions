class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        # fix 1 element
        res = []
        for k in range(0, len(nums) -2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums)-1

            while i < j:
                cur_sum = nums[k] + nums[i] + nums[j]
                if cur_sum == 0:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i+1] == nums[i]:                            
                        i += 1
                    while i < j and nums[j-1] == nums[j]:
                        j -= 1
                    i += 1
                    j -= 1

                elif cur_sum > 0:
                    j -= 1
                else:
                    i += 1
        
        return res
