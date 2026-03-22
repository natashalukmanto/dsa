from puzzle import Puzzle, Match
from collections import Counter

class Solver:
    def __init__(self, p):
        self.p = p
        self.guesses = []

    def _is_consistent(self, word, guess, result):
        for i, (g, m) in enumerate(zip(guess, result)):
            if m == Match.YES:
                if word[i] != g:
                    return False
            elif m == Match.MOVE:
                if word[i] == g or g not in word:
                    return False
            else:  # Match.NO
                if g in word:
                    yes_move_count = sum(
                        1 for j, (g2, m2) in enumerate(zip(guess, result))
                        if g2 == g and m2 in (Match.YES, Match.MOVE)
                    )
                    actual_count = word.count(g)
                    if actual_count != yes_move_count:
                        return False
        return True

    def solve_puzzle(self):
        length = self.p.answer_length()
        candidates = [w for w in self.p.eligible_words if len(w) == length]

        while not self.p.won():
            guess = candidates[0]
            result = self.p.guess(guess)
            self.guesses.append(guess)
            candidates = [w for w in candidates if self._is_consistent(w, guess, result)]

    def get_guesses(self):
        return self.guesses
