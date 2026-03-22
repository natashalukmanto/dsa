from __future__ import annotations

from typing import Dict, List, Optional

from document import Document


class WordCorpus:
    """Collection of documents indexed by doc_id.

    Provides the foundational storage and retrieval layer for
    the word analysis engine built on top of it.
    """

    def __init__(self) -> None:
        self._documents: Dict[str, Document] = {}

    def add_document(self, doc_id: str, text: str) -> None:
        """Register a new document. Overwrites if doc_id already exists."""
        self._documents[doc_id] = Document(doc_id=doc_id, text=text)

    def get_document(self, doc_id: str) -> Optional[Document]:
        """Return the Document for doc_id, or None if not found."""
        return self._documents.get(doc_id)

    def all_doc_ids(self) -> List[str]:
        """Return all registered doc IDs in insertion order."""
        return list(self._documents.keys())

    def has_document(self, doc_id: str) -> bool:
        return doc_id in self._documents
