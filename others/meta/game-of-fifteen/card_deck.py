from __future__ import annotations

from typing import List, Optional


class CardDeck:
    """Manages a collection of numeric card values in sequential order.

    Cards are stored internally and accessed via a first-in-first-out mechanism
    where the earliest card is considered the "top" of the deck.
    """

    def __init__(self, cards: List[int]):
        self._card_sequence: List[int] = [card_val for card_val in cards]

    def has_more(self) -> bool:
        card_count = len(self._card_sequence)
        return card_count > 0

    def draw(self) -> Optional[int]:
        """Extract and return the topmost card from the deck.

        If no cards remain, returns None instead of raising an error.
        """
        if not self.has_more():
            return None
        return self._card_sequence.pop(0)

    def remaining(self) -> List[int]:
        return [card for card in self._card_sequence]
