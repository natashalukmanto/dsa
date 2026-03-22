from __future__ import annotations

from collections import deque
from typing import List, Optional, Tuple

from cell import CellType
from maze_grid import MazeGrid

# Orthogonal movement directions: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class MazeRunner:
    """Grid traversal engine for mazes encoded as character grids.

    Starter code (already provided):
        from_strings, find_start, find_end

    Your tasks — implement the five methods marked below:
        Part 1 → is_passable
        Part 2 → get_neighbors
        Part 3 → find_shortest_path
        Part 4 → count_reachable_cells
        Part 5 → collect_items
    """

    def __init__(self, grid: MazeGrid) -> None:
        self.grid = grid

    # ------------------------------------------------------------------ #
    # Starter code — provided, do not modify                              #
    # ------------------------------------------------------------------ #

    @classmethod
    def from_strings(cls, rows: List[str]) -> "MazeRunner":
        """Construct a MazeRunner from a list of character-encoded strings."""
        return cls(MazeGrid.from_strings(rows))

    def find_start(self) -> Optional[Tuple[int, int]]:
        """Return the position of the START cell, or None if absent."""
        positions = self.grid.find_positions_of_type(CellType.START)
        return positions[0] if positions else None

    def find_end(self) -> Optional[Tuple[int, int]]:
        """Return the position of the END cell, or None if absent."""
        positions = self.grid.find_positions_of_type(CellType.END)
        return positions[0] if positions else None

    # ------------------------------------------------------------------ #
    # Part 1                                                              #
    # ------------------------------------------------------------------ #

    def is_passable(self, pos: Tuple[int, int]) -> bool:
        """Return True if pos is in bounds and its cell type is not WALL.

        Both out-of-bounds positions and WALL cells return False.

        Example (SIMPLE_MAZE in tests.py):
            is_passable((1, 1))  →  True    # START cell
            is_passable((0, 0))  →  False   # WALL
            is_passable((9, 9))  →  False   # out of bounds
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 2                                                              #
    # ------------------------------------------------------------------ #

    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Return all passable orthogonal neighbors of pos.

        Only considers the four cardinal directions (up/down/left/right).
        Results may be returned in any order.

        Example:
            get_neighbors((1, 1))  →  [(2, 1), (1, 2)]
                # walls and boundaries excluded
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 3                                                              #
    # ------------------------------------------------------------------ #

    def find_shortest_path(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> Optional[List[Tuple[int, int]]]:
        """Find the shortest path from start to end using BFS.

        Returns a list of positions from start to end (both inclusive),
        or None if end is unreachable from start.
        If start == end, return [start].

        Example:
            find_shortest_path((1,1), (4,4))  →  [(1,1), (1,2), ..., (4,4)]
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 4                                                              #
    # ------------------------------------------------------------------ #

    def count_reachable_cells(self, start: Tuple[int, int]) -> int:
        """Count all passable cells reachable from start (including start itself).

        Uses flood-fill (BFS) to find all connected passable cells.
        Returns 0 if start itself is not passable.

        Example (SIMPLE_MAZE):
            count_reachable_cells((1, 1))  →  14
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 5                                                              #
    # ------------------------------------------------------------------ #

    def collect_items(self, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Return the positions of all ITEM cells reachable from start,
        in the order they are first encountered during a BFS traversal.

        Items that are closer (in BFS distance) to start appear earlier.
        Ties at the same BFS depth may be returned in any order.

        Example (SIMPLE_MAZE, items at (3,1) and (3,4)):
            collect_items((1, 1))  →  [(3, 1), (3, 4)]
                # (3,1) is 2 hops away; (3,4) is 5 hops away
        """
        raise NotImplementedError
