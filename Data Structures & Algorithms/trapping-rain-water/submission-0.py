class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max = height[0] # the maximum height toward left side # l_max = 1 -> 2
        r_max = height[-1] # 7 -> 3

        water = 0
        while l < r:
            # l = 3 -> 4 
            if height[l] < height[r]: # always move the smaller one
                print(1, l ,r)
                top = min(l_max, height[r])
                water += top - height[l]
                l += 1
                l_max = max(l_max, height[l])
            else:
                print(2, l, r)
                top = min(r_max, height[l])
                water += top - height[r]
                r -= 1
                r_max = max(r_max, height[r])
            print(water)

        return water