from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Document:
    """Immutable representation of a text document.

    Stores the raw text; word tokenization is done lazily via words().
    Tokens are lowercased and split on any non-alphabetic character.
    """

    doc_id: str
    text: str

    def words(self) -> List[str]:
        """Return all tokens in the document (lowercased, alphabetic only)."""
        return [w for w in re.split(r"[^a-z]+", self.text.lower()) if w]
