class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False

        row = matrix[(top+bottom) // 2]
        left, right = 0, len(row) - 1

        while left <= right:
            m = (left + right) // 2
            item = row[m]
            if item > target:
                right = m - 1
            elif item < target:
                left = m + 1
            else:
                return True
        return False


