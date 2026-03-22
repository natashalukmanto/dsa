from __future__ import annotations

from typing import Iterable, List, Optional, Tuple

from cell import Cell, CellType


class MazeGrid:
    """Two-dimensional grid of cells parsed from a list of strings.

    Each character in the input maps to a CellType via its enum value.
    Row 0 is the topmost row; column 0 is the leftmost column.
    """

    def __init__(self, cells: List[List[Cell]]) -> None:
        self._cells = cells
        self._num_rows = len(cells)
        self._num_cols = len(cells[0]) if cells else 0

    @classmethod
    def from_strings(cls, rows: List[str]) -> "MazeGrid":
        """Parse a maze from a list of strings.

        Example input:
            ["######",
             "#S...#",
             "#.##.#",
             "#...E#",
             "######"]
        """
        cells: List[List[Cell]] = []
        for r, row_str in enumerate(rows):
            row: List[Cell] = []
            for c, ch in enumerate(row_str):
                row.append(Cell(row=r, col=c, cell_type=CellType(ch)))
            cells.append(row)
        return cls(cells)

    def num_rows(self) -> int:
        return self._num_rows

    def num_cols(self) -> int:
        return self._num_cols

    def in_bounds(self, pos: Tuple[int, int]) -> bool:
        r, c = pos
        return 0 <= r < self._num_rows and 0 <= c < self._num_cols

    def get_cell(self, pos: Tuple[int, int]) -> Optional[Cell]:
        """Return the cell at pos, or None if pos is out of bounds."""
        if not self.in_bounds(pos):
            return None
        r, c = pos
        return self._cells[r][c]

    def all_positions(self) -> Iterable[Tuple[int, int]]:
        """Yield every (row, col) in row-major order."""
        for r in range(self._num_rows):
            for c in range(self._num_cols):
                yield (r, c)

    def find_positions_of_type(self, cell_type: CellType) -> List[Tuple[int, int]]:
        """Return all positions whose cell type matches cell_type."""
        return [
            (r, c)
            for r, c in self.all_positions()
            if self._cells[r][c].cell_type == cell_type
        ]
