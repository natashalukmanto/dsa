from __future__ import annotations

from typing import Dict, List, Set, Tuple

from word_corpus import WordCorpus


class WordAnalyzer:
    """Text analytics engine built on a WordCorpus.

    Starter code (already provided):
        __init__, add_document

    Your tasks — implement the five methods marked below:
        Part 1 → unique_words
        Part 2 → top_k_frequent
        Part 3 → common_words
        Part 4 → maximize_coverage
        Part 5 → jaccard_similarity
    """

    def __init__(self) -> None:
        self.corpus = WordCorpus()

    # ------------------------------------------------------------------ #
    # Starter code — provided, do not modify                              #
    # ------------------------------------------------------------------ #

    def add_document(self, doc_id: str, text: str) -> None:
        """Add a document to the corpus."""
        self.corpus.add_document(doc_id, text)

    # ------------------------------------------------------------------ #
    # Part 1                                                              #
    # ------------------------------------------------------------------ #

    def unique_words(self, doc_id: str) -> Set[str]:
        """Return the set of distinct words appearing in document doc_id.

        Raises KeyError if doc_id is not in the corpus.

        Example:
            add_document("d1", "the cat sat on the mat")
            unique_words("d1")  →  {"the", "cat", "sat", "on", "mat"}
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 2                                                              #
    # ------------------------------------------------------------------ #

    def top_k_frequent(self, doc_id: str, k: int) -> List[Tuple[str, int]]:
        """Return the k most frequent words in doc_id as (word, count) tuples.

        Ranked by frequency descending; ties broken by word ascending.
        If k exceeds the number of distinct words, return all of them.

        Example:
            add_document("d1", "the cat sat on the mat the")
            top_k_frequent("d1", 2)  →  [("the", 3), ("cat", 1)]
                # "cat", "mat", "on", "sat" all have count 1; "cat" < others
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 3                                                              #
    # ------------------------------------------------------------------ #

    def common_words(self, doc_ids: List[str]) -> Set[str]:
        """Return the set of words that appear in ALL of the given documents.

        Returns an empty set if doc_ids is empty.
        Raises KeyError if any doc_id is not in the corpus.

        Example:
            add_document("d1", "the quick brown fox")
            add_document("d2", "the slow brown dog")
            add_document("d3", "the fast brown cat")
            common_words(["d1", "d2", "d3"])  →  {"the", "brown"}
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 4                                                              #
    # ------------------------------------------------------------------ #

    def maximize_coverage(self, budget: int, word_costs: Dict[str, int]) -> Set[str]:
        """Select a subset of words from word_costs to maximize the number of
        unique words chosen, subject to the total cost not exceeding budget.

        Each word may be selected at most once.
        Words not present in word_costs cannot be selected.
        Words with cost 0 are always free to include.

        Returns the set of selected words.

        Greedy insight: to maximize the *count* of unique words within a budget,
        always pick the cheapest words first (sort by cost ascending, then
        alphabetically for tie-breaking). This greedy is optimal here because
        every selected word contributes exactly +1 to the count regardless of cost.

        Example:
            word_costs = {"apple": 3, "bat": 1, "cat": 2, "dog": 5}
            maximize_coverage(budget=6, word_costs=word_costs)
            →  {"bat", "cat", "apple"}   # costs 1+2+3=6, picks 3 words
               (not {"bat", "cat", "dog"} which costs 1+2+5=8 > 6)
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 5                                                              #
    # ------------------------------------------------------------------ #

    def jaccard_similarity(self, doc_id_a: str, doc_id_b: str) -> float:
        """Compute the Jaccard similarity between two documents' word sets.

        Jaccard(A, B) = |A ∩ B| / |A ∪ B|

        Returns 0.0 if both documents are empty.
        Raises KeyError if either doc_id is not in the corpus.

        Example:
            add_document("d1", "cat dog bird")     # {cat, dog, bird}
            add_document("d2", "cat dog fish")     # {cat, dog, fish}
            jaccard_similarity("d1", "d2")
            →  2/4 = 0.5   # intersection={cat,dog}, union={cat,dog,bird,fish}
        """
        raise NotImplementedError
