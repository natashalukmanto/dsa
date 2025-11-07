from typing import List

def sortMatrix(grid: List[List[int]]) -> List[List[int]]:
    def sortDiagonals(r, c, reverse):
        values = getDiagonalValues(r, c)
        values.sort(reverse=reverse)
        for value in values:
            grid[r][c] = value
            r += 1
            c += 1

    def getDiagonalValues(r, c):
        values = []
        while r < n and c < n:
            values.append(grid[r][c])
            r += 1
            c += 1
        return values

    n = len(grid)
    for r in range(n-1):
        sortDiagonals(r, 0, reverse=True)
    for c in range(n-1, 0, -1):
        sortDiagonals(0, c, reverse=False)

    return grid

def sortMatrix0(grid: List[List[int]]) -> List[List[int]]:
    # bottom + middle -> decreasing order
    # upper -> increasing order

    # 3 x 3 matrix -> (0,2) and (2, 0) are unchanged
    # upper = (0, 1), (1, 2)
    # bottom = (0, 0), (1, 1), (2, 2)       (1, 0), (2, 1)
    # (0,0)
    n = len(grid)

    # sorting the top half
    for start_col in range(1, n - 1):
        r, c = 0, start_col
        part = []
        while r < n and c < n:
            part.append(grid[r][c])
            r += 1
            c += 1

        part.sort()
        r, c = 0, start_col
        while r < n and c < n:
            grid[r][c] = part[r]
            r += 1
            c += 1

    # sorting the bottom half
    for start_row in range(n - 1):
        r, c = start_row, 0
        part = []
        while r < n and c < n:
            part.append(grid[r][c])
            r += 1
            c += 1

        part.sort(reverse=True)
        r, c = start_row, 0
        while r < n and c < n:
            grid[r][c] = part[c]
            r += 1
            c += 1

    return grid
