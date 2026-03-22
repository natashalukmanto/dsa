import unittest

from word_analyzer import WordAnalyzer


# ------------------------------------------------------------------ #
# Part 1 — unique_words                                               #
# ------------------------------------------------------------------ #


class TestUniqueWords(unittest.TestCase):
    def setUp(self) -> None:
        self.wa = WordAnalyzer()
        self.wa.add_document("d1", "the cat sat on the mat")
        self.wa.add_document("d2", "the quick brown fox")
        self.wa.add_document("empty", "")

    def test_basic_unique_words(self) -> None:
        self.assertEqual(
            self.wa.unique_words("d1"), {"the", "cat", "sat", "on", "mat"}
        )

    def test_duplicates_deduplicated(self) -> None:
        # "the" appears twice in d1 but should appear once in the set
        result = self.wa.unique_words("d1")
        self.assertIn("the", result)
        self.assertEqual(len(result), 5)

    def test_case_insensitive(self) -> None:
        wa = WordAnalyzer()
        wa.add_document("doc", "Hello WORLD hello world")
        self.assertEqual(wa.unique_words("doc"), {"hello", "world"})

    def test_empty_document(self) -> None:
        self.assertEqual(self.wa.unique_words("empty"), set())

    def test_unknown_doc_raises_key_error(self) -> None:
        with self.assertRaises(KeyError):
            self.wa.unique_words("nonexistent")


# ------------------------------------------------------------------ #
# Part 2 — top_k_frequent                                             #
# ------------------------------------------------------------------ #


class TestTopKFrequent(unittest.TestCase):
    def setUp(self) -> None:
        self.wa = WordAnalyzer()
        self.wa.add_document("d1", "the cat sat on the mat the")

    def test_top_one(self) -> None:
        result = self.wa.top_k_frequent("d1", 1)
        self.assertEqual(result, [("the", 3)])

    def test_top_two(self) -> None:
        # "the" has 3; others have 1 each — "cat" is first alphabetically
        result = self.wa.top_k_frequent("d1", 2)
        self.assertEqual(result[0], ("the", 3))
        self.assertEqual(result[1][1], 1)  # second word has count 1

    def test_tie_broken_alphabetically(self) -> None:
        result = self.wa.top_k_frequent("d1", 6)
        # All words with count 1: cat, mat, on, sat — alphabetical order
        words_with_count_1 = [w for w, c in result if c == 1]
        self.assertEqual(words_with_count_1, sorted(words_with_count_1))

    def test_k_larger_than_vocab(self) -> None:
        result = self.wa.top_k_frequent("d1", 100)
        self.assertEqual(len(result), 5)  # only 5 distinct words

    def test_k_zero_returns_empty(self) -> None:
        self.assertEqual(self.wa.top_k_frequent("d1", 0), [])

    def test_single_word_repeated(self) -> None:
        wa = WordAnalyzer()
        wa.add_document("rep", "go go go")
        self.assertEqual(wa.top_k_frequent("rep", 1), [("go", 3)])


# ------------------------------------------------------------------ #
# Part 3 — common_words                                               #
# ------------------------------------------------------------------ #


class TestCommonWords(unittest.TestCase):
    def setUp(self) -> None:
        self.wa = WordAnalyzer()
        self.wa.add_document("d1", "the quick brown fox")
        self.wa.add_document("d2", "the slow brown dog")
        self.wa.add_document("d3", "the fast brown cat")

    def test_intersection_of_three(self) -> None:
        self.assertEqual(
            self.wa.common_words(["d1", "d2", "d3"]), {"the", "brown"}
        )

    def test_intersection_of_two(self) -> None:
        result = self.wa.common_words(["d1", "d2"])
        self.assertEqual(result, {"the", "brown"})

    def test_no_common_words(self) -> None:
        wa = WordAnalyzer()
        wa.add_document("a", "cat dog")
        wa.add_document("b", "fish bird")
        self.assertEqual(wa.common_words(["a", "b"]), set())

    def test_single_document_returns_its_own_words(self) -> None:
        result = self.wa.common_words(["d1"])
        self.assertEqual(result, {"the", "quick", "brown", "fox"})

    def test_empty_list_returns_empty_set(self) -> None:
        self.assertEqual(self.wa.common_words([]), set())

    def test_unknown_doc_raises_key_error(self) -> None:
        with self.assertRaises(KeyError):
            self.wa.common_words(["d1", "missing"])


# ------------------------------------------------------------------ #
# Part 4 — maximize_coverage                                          #
# ------------------------------------------------------------------ #


class TestMaximizeCoverage(unittest.TestCase):
    def setUp(self) -> None:
        self.word_costs = {"apple": 3, "bat": 1, "cat": 2, "dog": 5, "eel": 4}

    def test_basic_greedy(self) -> None:
        wa = WordAnalyzer()
        result = wa.maximize_coverage(6, self.word_costs)
        # Sorted by cost: bat(1), cat(2), apple(3), eel(4), dog(5)
        # Pick: bat(1) + cat(2) + apple(3) = 6 → 3 words
        self.assertEqual(result, {"bat", "cat", "apple"})

    def test_exact_budget(self) -> None:
        wa = WordAnalyzer()
        result = wa.maximize_coverage(1, self.word_costs)
        self.assertEqual(result, {"bat"})

    def test_zero_budget(self) -> None:
        wa = WordAnalyzer()
        result = wa.maximize_coverage(0, self.word_costs)
        self.assertEqual(result, set())

    def test_large_budget_picks_all(self) -> None:
        wa = WordAnalyzer()
        result = wa.maximize_coverage(100, self.word_costs)
        self.assertEqual(result, {"apple", "bat", "cat", "dog", "eel"})

    def test_free_words_always_included(self) -> None:
        wa = WordAnalyzer()
        costs = {"free": 0, "cheap": 1, "pricey": 999}
        result = wa.maximize_coverage(0, costs)
        self.assertIn("free", result)
        self.assertNotIn("cheap", result)

    def test_count_maximized_not_value(self) -> None:
        # budget=3: picking "bat"(1)+"cat"(2)=3 gives 2 words,
        # which beats "dog"(5) which only gives 1 word (but costs more anyway)
        wa = WordAnalyzer()
        result = wa.maximize_coverage(3, self.word_costs)
        self.assertEqual(len(result), 2)
        self.assertIn("bat", result)
        self.assertIn("cat", result)


# ------------------------------------------------------------------ #
# Part 5 — jaccard_similarity                                         #
# ------------------------------------------------------------------ #


class TestJaccardSimilarity(unittest.TestCase):
    def setUp(self) -> None:
        self.wa = WordAnalyzer()
        self.wa.add_document("d1", "cat dog bird")
        self.wa.add_document("d2", "cat dog fish")
        self.wa.add_document("d3", "lion tiger bear")
        self.wa.add_document("d4", "cat dog bird")  # identical to d1

    def test_partial_overlap(self) -> None:
        # intersection={cat,dog}, union={cat,dog,bird,fish} → 2/4 = 0.5
        self.assertAlmostEqual(self.wa.jaccard_similarity("d1", "d2"), 0.5)

    def test_no_overlap(self) -> None:
        self.assertAlmostEqual(self.wa.jaccard_similarity("d1", "d3"), 0.0)

    def test_identical_documents(self) -> None:
        self.assertAlmostEqual(self.wa.jaccard_similarity("d1", "d4"), 1.0)

    def test_symmetric(self) -> None:
        self.assertAlmostEqual(
            self.wa.jaccard_similarity("d1", "d2"),
            self.wa.jaccard_similarity("d2", "d1"),
        )

    def test_both_empty_returns_zero(self) -> None:
        wa = WordAnalyzer()
        wa.add_document("e1", "")
        wa.add_document("e2", "")
        self.assertAlmostEqual(wa.jaccard_similarity("e1", "e2"), 0.0)

    def test_unknown_doc_raises_key_error(self) -> None:
        with self.assertRaises(KeyError):
            self.wa.jaccard_similarity("d1", "missing")


if __name__ == "__main__":
    unittest.main()
