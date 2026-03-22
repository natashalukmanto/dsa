import unittest
from puzzle import Puzzle
from solver import Solver


class SolverTest(unittest.TestCase):
    def setUp(self):
        self.subject = None

    def test_should_solve_simple_case(self):
        p = Puzzle("easy")
        self.subject = Solver(p)
        self.subject.solve_puzzle()
        self.assertTrue(p.won(), "couldn't guess 'easy'")
        self.assertEqual(len(self.subject.get_guesses()), p.num_guesses(), "don't cheat!")
        self.assertTrue(p.num_guesses() < 7, "don't guess too much")

    def test_should_be_an_optimal_guesser(self):
        test_words = ["easy", "hard", "dock", "drop", "dome", "area", "arms",
                      "atom", "avid", "away"]
        total_guesses = 0
        solved_count = 0

        for answer in test_words:
            p = Puzzle(answer)
            solver = Solver(p)
            solver.solve_puzzle()

            if p.won():
                total_guesses += p.num_guesses()
                solved_count += 1
            else:
                print(f"Warning: Failed to solve '{answer}'")

        if solved_count == 0:
            self.fail("Solver couldn't solve any puzzles!")

        average_guesses = total_guesses / solved_count
        self.assertTrue(
            average_guesses < 4.0,
            f"Average guesses: {average_guesses:.2f}, expected < 4.0. "
            f"Solved {solved_count}/{len(test_words)} puzzles.",
        )


if __name__ == "__main__":
    unittest.main()
