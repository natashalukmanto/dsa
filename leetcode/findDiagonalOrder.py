from typing import List

def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    if not mat or not mat[0]:
        return []

    N, M = len(mat), len(mat[0])
    row, column = 0, 0
    direction = 1
    result = []

    while row < N and column < M:
        result.append(mat[row][column])

        new_row = row + (-1 if direction else 1)
        new_column = column + (1 if direction else -1)

        if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
            if direction:
                row += column == M - 1
                column += column < M - 1
            else:
                column += row == N - 1
                row += row < N - 1

            direction ^= 1
        else:
            row = new_row
            column = new_column

    return result

    # res = []
    # rows, cols = len(mat), len(mat[0])

    # iteration, curr_cell = 1, [0, 0]
    # while len(res) < rows * cols:
    #     if iteration % 2 != 0:  # direction = down-left
    #         while curr_cell[0] < rows and curr_cell[1] > -1:
    #             res.append(mat[curr_cell[0]][curr_cell[1]])
    #             curr_cell[0] += 1
    #             curr_cell[1] -= 1
    #         # undo overshoot to last valid cell
    #         curr_cell[0] -= 1
    #         curr_cell[1] += 1
    #         # bump based on wall hit
    #         if curr_cell[0] == rows - 1:  # bottom wall
    #             curr_cell[1] += 1          # go right
    #         else:                          # left wall
    #             curr_cell[0] += 1          # go down
    #     else:  # direction = up-right
    #         while curr_cell[0] > -1 and curr_cell[1] < cols:
    #             res.append(mat[curr_cell[0]][curr_cell[1]])
    #             curr_cell[0] -= 1
    #             curr_cell[1] += 1
    #         # undo overshoot to last valid cell
    #         curr_cell[0] += 1
    #         curr_cell[1] -= 1
    #         # bump based on wall hit
    #         if curr_cell[1] == cols - 1:  # right wall
    #             curr_cell[0] += 1          # go down
    #         else:                          # top wall
    #             curr_cell[1] += 1          # go right
    #     iteration += 1

    # return res
