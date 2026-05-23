class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # since there is a range for the nums[i] val, we can create a bucket array for it
        bucket_arr = [0] * 2001
        for num in nums:
            bucket_arr[num+1000] += 1
        
        res = []
        # Traverse the bucket list for K times and find out the top K elements.
        for _ in range(k):
            # max freq and it's idx - 1000 of this round
            local_max = float('-inf')
            max_idx = -99999
            for idx, freq in enumerate(bucket_arr):
                if freq > local_max:
                    local_max = freq
                    max_idx = idx - 1000
            
            bucket_arr[max_idx + 1000] = 0
            res.append(max_idx)

        return res