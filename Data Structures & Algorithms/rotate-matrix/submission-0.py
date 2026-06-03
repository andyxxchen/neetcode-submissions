'''
    def rotate(self, matrix: List[List[int]]) -> None:
    Input: matrix = [
    [1,2],
    [3,4]
    ]

    [
    [3,4],
    [1,2]
    ]

    (0, 2) <-> (1, 0)

    Output: [
    [3,1],
    [4,2]
    ]
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    