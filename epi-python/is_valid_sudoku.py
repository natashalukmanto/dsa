from typing import List

"""
Quoted from the book: There is no real scope for algorithm optimization in this problem, it's all about writing clean code. 
"""

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku0(partial_assignment: List[List[int]]) -> bool:
    # Checking each row
    for i in range(9):
        row_set = set()
        for j in range(9):
            row = partial_assignment[i][j]
            if row == 0: continue
            if row in row_set:
                return False
            row_set.add(row)
            
    # Checking each column
    for i in range(9):
        col_set = set()
        for j in range(9):
            col = partial_assignment[j][i]
            if col == 0: continue
            if col in col_set:
                return False
            col_set.add(col)


    # Checking the 3x3 2D subarray
    for row_jump in range(0, 9, 3):
        for col_jump in range(0, 9, 3):
            box_set = set()
            for i in range(3):
                for j in range(3):
                    if partial_assignment[row_jump + i][col_jump + j] == 0: continue
                    if partial_assignment[row_jump + i][col_jump + j] in box_set:
                        return False
                    box_set.add(partial_assignment[row_jump + i][col_jump + j])
            
    return True

def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def has_duplicate(block) -> bool:
        