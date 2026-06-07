class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force -> for each mid point, expand both size, max(res, cur_max)
        # n^2

        n = len(heights)
        # for each index find the nearest left element that's shorter than the current one
        leftMax = [-1] * n
        stack = []
        # increasing monotonic stack is to find the first small element on the left side
        for i in range(n):
            cur = heights[i]
            while stack and heights[stack[-1]] >= cur:
                stack.pop()
            if stack:
                leftMax[i] = stack[-1]
            stack.append(i)
        
        # for each index find the nearest right element that's shorter than the current one
        rightMax = [n] * n
        stack = []
        # increasing monotonic stack is to find the first small element on the left side
        for i in range(n-1, -1, -1):
            cur = heights[i]
            while stack and heights[stack[-1]] >= cur:
                stack.pop()
            if stack:
                rightMax[i] = stack[-1]
            stack.append(i)
        print(leftMax)
        print(rightMax)

        res = 0
        # traverse the whole array once to calculate each rectangle
        for i in range(n):
            res = max(res, heights[i] * (rightMax[i] - leftMax[i] - 1))
        
        return res