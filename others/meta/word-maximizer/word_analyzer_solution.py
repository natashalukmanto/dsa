from __future__ import annotations

from typing import Dict, List, Set, Tuple

from word_corpus import WordCorpus


class WordAnalyzer:
    def __init__(self) -> None:
        self.corpus = WordCorpus()

    def add_document(self, doc_id: str, text: str) -> None:
        self.corpus.add_document(doc_id, text)

    def unique_words(self, doc_id: str) -> Set[str]:
        doc = self.corpus.get_document(doc_id)
        if doc is None:
            raise KeyError(doc_id)
        return set(doc.words())

    def top_k_frequent(self, doc_id: str, k: int) -> List[Tuple[str, int]]:
        doc = self.corpus.get_document(doc_id)
        if doc is None:
            raise KeyError(doc_id)
        counts: Dict[str, int] = {}
        for word in doc.words():
            counts[word] = counts.get(word, 0) + 1
        return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]

    def common_words(self, doc_ids: List[str]) -> Set[str]:
        if not doc_ids:
            return set()
        result = self.unique_words(doc_ids[0])
        for doc_id in doc_ids[1:]:
            result &= self.unique_words(doc_id)
        return result

    def maximize_coverage(self, budget: int, word_costs: Dict[str, int]) -> Set[str]:
        selected: Set[str] = set()
        remaining = budget
        for word, cost in sorted(word_costs.items(), key=lambda x: (x[1], x[0])):
            if cost <= remaining:
                selected.add(word)
                remaining -= cost
        return selected

    def jaccard_similarity(self, doc_id_a: str, doc_id_b: str) -> float:
        set_a = self.unique_words(doc_id_a)
        set_b = self.unique_words(doc_id_b)
        union = set_a | set_b
        if not union:
            return 0.0
        return len(set_a & set_b) / len(union)
