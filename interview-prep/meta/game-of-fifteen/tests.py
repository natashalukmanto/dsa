import unittest

from card_deck import CardDeck
from card_table import CardTable
from sum_15_game import Sum15Game


class TestCardDeckDrawing(unittest.TestCase):
    def test_deck_draws_different_cards(self) -> None:
        """Test that drawing from deck consumes cards and returns different values."""
        deck_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        deck = CardDeck(deck_values)
        table = CardTable.from_deck(rows=3, cols=3, deck=deck)

        self.assertEqual(table.get((0, 0)), 1, "First card should be 1")
        self.assertEqual(table.get((0, 1)), 2, "Second card should be 2")
        self.assertEqual(table.get((0, 2)), 3, "Third card should be 3")
        self.assertEqual(table.get((1, 0)), 4, "Fourth card should be 4")
        self.assertEqual(table.get((1, 1)), 5, "Fifth card should be 5")
        self.assertEqual(table.get((1, 2)), 6, "Sixth card should be 6")
        self.assertEqual(table.get((2, 0)), 7, "Seventh card should be 7")
        self.assertEqual(table.get((2, 1)), 8, "Eighth card should be 8")
        self.assertEqual(table.get((2, 2)), 9, "Ninth card should be 9")

        self.assertFalse(deck.has_more(), "Deck should be empty after drawing 9 cards")
        self.assertEqual(deck.remaining(), [], "Deck should have no remaining cards")

    def test_deck_draw_consumes_cards(self) -> None:
        """Test that draw() actually removes cards from the deck."""
        deck = CardDeck([10, 20, 30])

        first = deck.draw()
        self.assertEqual(first, 10)
        self.assertEqual(deck.remaining(), [20, 30], "First card should be removed")

        second = deck.draw()
        self.assertEqual(second, 20)
        self.assertEqual(deck.remaining(), [30], "Second card should be removed")

    def test_deck_draw_returns_none_when_empty(self) -> None:
        """Test that draw() returns None when no cards remain."""
        deck = CardDeck([])
        self.assertIsNone(deck.draw())

    def test_table_partial_fill_when_deck_runs_out(self) -> None:
        """Test that cells remain None when the deck has fewer cards than cells."""
        deck = CardDeck([1, 2, 3])
        table = CardTable.from_deck(rows=2, cols=3, deck=deck)

        self.assertEqual(table.get((0, 0)), 1)
        self.assertEqual(table.get((0, 1)), 2)
        self.assertEqual(table.get((0, 2)), 3)
        self.assertIsNone(table.get((1, 0)))
        self.assertIsNone(table.get((1, 1)))
        self.assertIsNone(table.get((1, 2)))


class TestMoveValidation(unittest.TestCase):
    def test_valid_move_succeeds(self) -> None:
        # 3x3 grid, first row: 4, 5, 6
        deck_values = [4, 5, 6, 1, 1, 1, 2, 2, 2]
        game = Sum15Game(rows=3, cols=3, deck_values=deck_values)
        positions = [(0, 0), (0, 1), (0, 2)]
        self.assertTrue(game.is_valid_move(positions))

    def test_duplicate_positions_rejected(self) -> None:
        deck_values = [4, 5, 6, 1, 1, 1, 2, 2, 2]
        game = Sum15Game(rows=3, cols=3, deck_values=deck_values)
        positions = [(0, 0), (0, 0), (0, 1)]
        self.assertFalse(game.is_valid_move(positions))

    def test_empty_cells_rejected(self) -> None:
        # Start with a grid where some cells are empty (None).
        deck_values = [4, 5, 6]
        game = Sum15Game(rows=2, cols=3, deck_values=deck_values)
        # All cards are in row 0, row 1 is empty.
        positions = [(0, 0), (1, 1), (0, 2)]
        self.assertFalse(game.is_valid_move(positions))

    def test_duplicate_positions_with_sum_15_rejected(self) -> None:
        # Deck chosen so that using the same position twice would (incorrectly)
        # form a sum of 15 if duplicates were allowed: 5 + 5 + 5 = 15.
        deck_values = [5, 5, 5]
        game = Sum15Game(rows=1, cols=3, deck_values=deck_values)
        positions = [(0, 0), (0, 0), (0, 1)]
        self.assertFalse(
            game.is_valid_move(positions),
            "Moves that reuse a position should be rejected even if the values sum to 15.",
        )

    def test_empty_cell_that_would_complete_sum_to_15_is_rejected(self) -> None:
        # Deck chosen so that treating an empty cell as 0 would make the sum 15:
        # table row is [10, 5, None].
        deck_values = [10, 5]
        game = Sum15Game(rows=1, cols=3, deck_values=deck_values)
        positions = [(0, 0), (0, 1), (0, 2)]
        self.assertFalse(
            game.is_valid_move(positions),
            "Moves that include an empty cell must be rejected even if 0 would complete the sum to 15.",
        )


class TestApplyMove(unittest.TestCase):
    def test_apply_move_refills_all_empty_cells(self) -> None:
        # Deck chosen so that the first row forms a valid triple (4 + 5 + 6 = 15)
        # and there are extra cards to refill.
        deck_values = [4, 5, 6, 1, 1, 1, 2, 2, 2, 9, 9, 9, 9]
        game = Sum15Game(rows=3, cols=3, deck_values=deck_values)
        move = [(0, 0), (0, 1), (0, 2)]

        # Manually clear one more cell to simulate a previous removal.
        game.card_table.set((1, 1), None)

        game.apply_move(move)

        # After applying a move, all empty cells should have been
        # refilled in row-major order, as long as the deck has cards.
        empties = [
            pos
            for pos in game.card_table.positions_row_major()
            if game.card_table.get(pos) is None
        ]
        self.assertEqual([], empties, "All empty cells should have been refilled.")


class TestSearch(unittest.TestCase):
    def test_find_any_valid_move_returns_triple_when_exists(self) -> None:
        # Construct a deck so that the grid has at least one valid move.
        deck_values = [7, 4, 4, 1, 1, 1]
        game = Sum15Game(rows=2, cols=3, deck_values=deck_values)

        triple = game.find_any_valid_move()
        self.assertIsNotNone(triple, "A valid move should exist.")
        if triple is not None:
            self.assertTrue(game.is_valid_move(triple))

    def test_find_any_valid_move_returns_none_when_no_move(self) -> None:
        # No three cards can sum to 15.
        deck_values = [10, 10, 10, 11, 11, 11]
        game = Sum15Game(rows=2, cols=3, deck_values=deck_values)

        triple = game.find_any_valid_move()
        self.assertIsNone(triple, "No valid move should exist.")


class TestSolver(unittest.TestCase):
    def test_solve_to_end_plays_until_no_moves_remain(self) -> None:
        # Grid after deal:
        #   4 5 6
        #   9 9 9
        #   8 8 8
        # Only one valid move exists: (4, 5, 6) in the first row.
        deck_values = [4, 5, 6, 9, 9, 9, 8, 8, 8]
        game = Sum15Game(rows=3, cols=3, deck_values=deck_values)

        moves = game.solve_to_end()
        self.assertEqual(1, moves)

    def test_solve_to_end_returns_zero_when_no_moves(self) -> None:
        deck_values = [10, 10, 10, 11, 11, 11]
        game = Sum15Game(rows=2, cols=3, deck_values=deck_values)

        moves = game.solve_to_end()
        self.assertEqual(0, moves)


if __name__ == "__main__":
    unittest.main()
