from typing import List

def equalPairs(self, grid: List[List[int]]) -> int:
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
