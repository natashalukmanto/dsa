from __future__ import annotations

from typing import List, Optional, Tuple

from card_deck import CardDeck
from card_table import CardTable


class Sum15Game:
    """Game controller implementing the Sum-15 puzzle mechanics.

    Players select three card positions that sum to a target value.
    The game manages deck distribution and board state transitions.
    """

    TARGET_SUM = 15

    def __init__(self, rows: int, cols: int, deck_values: List[int]):
        self.deck = CardDeck(deck_values)
        self.card_table = CardTable.from_deck(rows, cols, self.deck)

    def is_valid_move(self, positions: List[Tuple[int, int]]) -> bool:
        """Determine whether a move selection meets all game rules.

        Validation checks include: position count, boundary constraints,
        uniqueness requirements, card presence, and sum calculation.
        """
        # uniqueness requirements & # position count
        if len(positions) != len(set(positions)): return False
        
        # boundary constraints
        for position in positions:
            if not self.card_table.in_bounds(position): 
                return False

        # card presence & sum calculation
        res = 0
        for position in positions:
            if self.card_table.get(position) is not None:
                res += self.card_table.get(position)
            else:
                return False
        if res != 15: return False
        
        return True
            
    def _clear_selected_positions(self, positions: List[Tuple[int, int]]) -> None:
        for position in positions:
            self.card_table.set(position, None)

    def _refill_empty_cells(self, positions: List[Tuple[int, int]]) -> None:
        for pos in self.card_table.positions_row_major():
            if self.card_table.get(pos) is None:
                if self.deck.has_more():
                    self.card_table.set(pos, self.deck.draw())
                else:
                    return

    def apply_move(self, positions: List[Tuple[int, int]]) -> None:
        """Execute a move by clearing selected cards and replenishing the board.

        The process involves two phases: first removing cards at selected
        positions, then systematically refilling all empty cells from the deck.
        """
        self._clear_selected_positions(positions)
        self._refill_empty_cells(positions)

    def _build_active_cell_index(self) -> List[Tuple[Tuple[int, int], int]]:
        raise NotImplementedError

    def find_any_valid_move(self) -> Optional[List[Tuple[int, int]]]:
        """Search for any valid three-card combination summing to the target."""
        all_positions: List[Tuple[int, int]] = list(self.card_table.positions_row_major())
        n = len(all_positions)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    triple = [all_positions[i], all_positions[j], all_positions[k]]
                    if self.is_valid_move(triple):
                        return triple

    def solve_to_end(self) -> int:
        """Automatically play moves until the game reaches a terminal state.

        Implements a greedy strategy: repeatedly find and execute any
        available valid move until no further moves are possible.
        Returns the total number of moves executed during the solve.
        """
        total_moves = 0
        
        while True:
            move = self.find_any_valid_move()
            if move is None: break
            
            self.apply_move(move)
            total_moves += 1
        
        return total_moves
