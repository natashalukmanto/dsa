from __future__ import annotations

from collections import deque
from typing import List, Optional, Tuple

from cell import CellType
from maze_grid import MazeGrid

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class MazeRunner:
    def __init__(self, grid: MazeGrid) -> None:
        self.grid = grid

    @classmethod
    def from_strings(cls, rows: List[str]) -> "MazeRunner":
        return cls(MazeGrid.from_strings(rows))

    def find_start(self) -> Optional[Tuple[int, int]]:
        positions = self.grid.find_positions_of_type(CellType.START)
        return positions[0] if positions else None

    def find_end(self) -> Optional[Tuple[int, int]]:
        positions = self.grid.find_positions_of_type(CellType.END)
        return positions[0] if positions else None

    def is_passable(self, pos: Tuple[int, int]) -> bool:
        cell = self.grid.get_cell(pos)
        return cell is not None and cell.cell_type != CellType.WALL

    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        r, c = pos
        return [
            (r + dr, c + dc)
            for dr, dc in DIRECTIONS
            if self.is_passable((r + dr, c + dc))
        ]

    def find_shortest_path(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> Optional[List[Tuple[int, int]]]:
        if start == end:
            return [start]
        queue: deque[List[Tuple[int, int]]] = deque([[start]])
        visited = {start}
        while queue:
            path = queue.popleft()
            for neighbor in self.get_neighbors(path[-1]):
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def count_reachable_cells(self, start: Tuple[int, int]) -> int:
        if not self.is_passable(start):
            return 0
        visited = {start}
        queue: deque[Tuple[int, int]] = deque([start])
        while queue:
            for neighbor in self.get_neighbors(queue.popleft()):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited)

    def collect_items(self, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        items: List[Tuple[int, int]] = []
        visited = {start}
        queue: deque[Tuple[int, int]] = deque([start])
        while queue:
            pos = queue.popleft()
            cell = self.grid.get_cell(pos)
            if cell and cell.cell_type == CellType.ITEM:
                items.append(pos)
            for neighbor in self.get_neighbors(pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return items
