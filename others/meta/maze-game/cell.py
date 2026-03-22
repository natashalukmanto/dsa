from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class CellType(Enum):
    """Character encoding used in string-based maze definitions."""

    OPEN = "."
    WALL = "#"
    START = "S"
    END = "E"
    ITEM = "I"


@dataclass(frozen=True)
class Cell:
    """Immutable value object representing a single maze tile."""

    row: int
    col: int
    cell_type: CellType

    @property
    def position(self) -> Tuple[int, int]:
        return (self.row, self.col)
