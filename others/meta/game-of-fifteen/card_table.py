from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple, Iterable

from card_deck import CardDeck


@dataclass(frozen=True)
class CardTable:
    """Two-dimensional matrix representing card placements on a game board.

    Each cell can contain either a numeric card value or None to indicate
    an unoccupied slot.
    """

    rows: int
    cols: int
    cells: List[List[Optional[int]]]

    @classmethod
    def from_deck(instance, rows: int, cols: int, deck: CardDeck) -> "CardTable":
        """Construct a table by distributing cards from the deck.

        Distribution follows a top-to-bottom, left-to-right pattern.
        Insufficient cards result in trailing cells remaining vacant.
        """
        grid_layout: List[List[Optional[int]]] = []
        for row_index in range(rows):
            current_row: List[Optional[int]] = []
            for col_index in range(cols):
                drawn_card = deck.draw()
                current_row.append(drawn_card)
            grid_layout.append(current_row)
        return instance(rows=rows, cols=cols, cells=grid_layout)

    def in_bounds(self, pos: Tuple[int, int]) -> bool:
        (row_idx, col_idx) = pos
        row_valid = row_idx >= 0 and row_idx < self.rows
        col_valid = col_idx >= 0 and col_idx < self.cols
        return row_valid and col_valid

    def get(self, pos: Tuple[int, int]) -> Optional[int]:
        (row_idx, col_idx) = pos
        return self.cells[row_idx][col_idx]

    def set(self, pos: Tuple[int, int], value: Optional[int]) -> None:
        (row_idx, col_idx) = pos
        self.cells[row_idx][col_idx] = value

    def positions_row_major(self) -> Iterable[Tuple[int, int]]:
        for row_idx in range(self.rows):
            for col_idx in range(self.cols):
                yield (row_idx, col_idx)
