from typing import List
from collections import deque

def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[-1][-1] != 0 or grid[0][0] != 0: return -1

    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_neighbors(row, col):
        for x, y in directions:
            new_row = row + x
            new_col = col + y

            if not (0 <= new_row <= max_row and 0 <= new_col <= max_col) or grid[new_row][new_col] != 0:
                continue

            yield(new_row, new_col)
    
    queue = deque()
    queue.append((0, 0))
    grid[0][0] = 1

    while queue:
        row, col = queue.popleft()
        distance = grid[row][col]

        if row == max_row and col == max_col:
            return distance
        
        for neighbor_row, neighbor_col in get_neighbors(row, col):
            grid[neighbor_row][neighbor_col] = distance + 1
            queue.append((neighbor_row, neighbor_col))
        
    return -1

def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[-1][-1] != 0 or grid[0][0] != 0: return -1

    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_neighbors(row, col):
        for x, y in directions:
            new_row = row + x
            new_col = col + y

            if not (0 <= new_row <= max_row and 0 <= new_col <= max_col) or grid[new_row][new_col] != 0:
                continue

            yield(new_row, new_col)
    
    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}

    while queue:
        row, col, distance = queue.popleft()

        if row == max_row and col == max_col:
            return distance
        
        for neighbor in get_neighbors(row, col):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            neighbor_row, neighbor_col = neighbor
            queue.append((neighbor_row, neighbor_col, distance + 1))
        
    return -1