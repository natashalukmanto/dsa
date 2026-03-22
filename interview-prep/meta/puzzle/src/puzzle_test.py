import unittest
from puzzle import Puzzle, Match


class PuzzleTest(unittest.TestCase):
    def test_check(self):
        all_cases = [
            # answer, guess, result
            Case("atom", "aloha", "wrong length"),
            Case("atom", "atim", "not a word"),
            Case("dock", "dock", "YYYY"),
            Case("dock", "drop", "YNMN"),
            Case("dock", "dome", "YYNN"),
            Case("dock", "abcd", "not a word"),
            Case("dock", "doff", "YYNN"),
            Case("dock", "dodo", "YYNN"), # trouble: FIXED
            Case("dock", "able", "NNNN"),
            Case("atom", "mota", "MMMM"),
            Case("dog",  "oog",  "NYY"), # trouble
            Case("aab", "aac", "YYN")
        ]

        failures = []
        for tc in all_cases:
            puzzle = Puzzle(tc.answer)
            actual_str = None
            try:
                actual = puzzle.guess(tc.guess)
                actual_str = match_array_to_string(actual)
            except ValueError as e:
                actual_str = str(e)

            if tc.expected != actual_str:
                failures.append(
                    f"\n  answer={tc.answer}, guess={tc.guess}, "
                    f"got '{actual_str}' instead of '{tc.expected}'"
                )

        if failures:
            self.fail("=== TEST CASE FAILURES ===" + "".join(failures) + "\n=== END ===")


class Case:
    def __init__(self, answer, guess, expected):
        self.answer = answer
        self.guess = guess
        self.expected = expected


def match_array_to_string(matches):
    sb = []
    for match in matches:
        if match == Match.YES:
            sb.append("Y")
        elif match == Match.MOVE:
            sb.append("M")
        else:
            sb.append("N")
    return "".join(sb)


if __name__ == "__main__":
    unittest.main()
