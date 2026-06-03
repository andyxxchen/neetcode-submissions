'''
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]

'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # all should be n * n
        m = len(matrix)
        n = len(matrix[0])

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        # if m == 1:
        #     return matrix[0]

        res = []
        i = 0
        j = 0
        # inclusive boundary
        top, right, left, bottom = 0, n-1, 0, m-1
        while left <= right and top <= bottom:
            # top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # left column
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1



        return res
            
