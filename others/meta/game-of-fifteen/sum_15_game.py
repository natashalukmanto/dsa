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
        valid_cells = []
        for position in self.card_table.positions_row_major():
            card_value = self.card_table.get(position)
            if card_value is not None:
                valid_cells.append((position, card_value))
        
        if len(valid_cells) < 3:
            return None
        
        for first_idx in range(len(valid_cells)):
            first_position, first_value = valid_cells[first_idx]
            value_to_index_map: dict[int, int] = {}
            
            for second_idx in range(first_idx + 1, len(valid_cells)):
                second_position, second_value = valid_cells[second_idx]
                
                third_idx = value_to_index_map.get(self.TARGET_SUM - first_value - second_value)
                
                if third_idx is not None:
                    third_position, _ = valid_cells[third_idx]
                    candidate_triple = [first_position, second_position, third_position]
                    if self.is_valid_move(candidate_triple):
                        return candidate_triple
                
                value_to_index_map[second_value] = second_idx
        
        return None
        
        
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
