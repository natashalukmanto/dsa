from typing import List

# Optimized, but not one pass
def searchMatrix1(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    left, right, bottom, top = 0, cols, 0, rows

    # Binary search on the rows
    while bottom <= top: # bottom starts from rows[0], top is row rows[-1]
        middle_row = bottom + (top - bottom) // 2
        print("Binary search on the rows", matrix[middle_row][0])
        if matrix[middle_row][0] > target:
            top = middle_row - 1
        elif matrix[middle_row][-1] < target:
            bottom = middle_row + 1
        else:
            break
    
    if (bottom > top): return False

    row = bottom + (top - bottom) // 2
        
    # Binary search on the columns
    while left <= right: # left starts from cols[0], right is row cols[-1]
        middle_col = left + (right - left) // 2
        if matrix[row][middle_col] == target:
            return True
        elif matrix[row][middle_col] < target:
            left = middle_col + 1
        else:
            right = middle_col - 1

    return False

# One pass
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols

    while left < right:
        middle = left + (right - left) // 2
        row, col = middle // cols, middle % cols
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = middle
        else:
            left = middle + 1
    
    return False
