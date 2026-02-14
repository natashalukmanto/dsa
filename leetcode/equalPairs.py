from typing import List
from collections import Counter


def equalPairs(grid: List[List[int]]) -> int:
    matches, n = 0, len(grid)
    group = {}

    for g in grid:
        group[tuple(g)] = group.get(tuple(g), 0) + 1

    for col in range(n):

        g = []
        for row in range(n):
            g.append(grid[row][col])

        if tuple(g) in group:
            matches += group[tuple(g)]

    return matches


def equalPairs(grid: List[List[int]]) -> int:
    res, n = 0, len(grid)
    row_counter = Counter(tuple(row) for row in grid)

    for c in range(n):
        col = list(grid[i][c] for i in range(n))
        res += row_counter[tuple(col)]

    return res
