class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while i <= j and i < len(matrix) and j >= 0:
            m = i + (j-i) // 2
            if matrix[m][0] > target:
                j = m - 1
            elif matrix[m][0] < target:
                i = m + 1
            else:
                return True
            
        # i = 1 and j = 0 => j is the row where the target is at
        row = j
        i = 0
        j = len(matrix[row]) - 1
        while i <= j and i < len(matrix[row]) and j >= 0:
            m = i + (j-i) // 2
            if matrix[row][m] > target:
                j = m - 1
            elif matrix[row][m] < target:
                i = m + 1
            else:
                return True
        return False
        


        