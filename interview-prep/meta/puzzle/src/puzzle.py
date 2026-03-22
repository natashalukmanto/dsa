from enum import Enum
from dictionary import Dictionary


class Match(Enum):
    YES = "YES"
    NO = "NO"
    MOVE = "MOVE"


class Puzzle:
    def __init__(self, answer):
        self.answer = list(answer)
        self.eligible_words = Dictionary.get_test_dictionary()
        self._won = False
        self.lost = False
        self._num_guesses = 0

    def answer_length(self):
        return len(self.answer)

    def _check_guess(self, guess):
        guess_chars = list(guess)
        result = [Match.NO] * len(self.answer)

        for idx in range(len(self.answer)):
            result[idx] = Match.NO
            if guess_chars[idx] == self.answer[idx]:
                result[idx] = Match.YES
            else:
                for others in range(len(self.answer)):
                    if guess_chars[idx] == self.answer[others]:
                        result[idx] = Match.MOVE
                        break

        return result

    def guess(self, guess):
        if self.lost:
            raise RuntimeError("game over")
        if len(guess) != len(self.answer):
            raise ValueError("wrong length")
        if guess not in self.eligible_words:
            raise ValueError("not a word")

        result = self._check_guess(guess)
        if all(m == Match.YES for m in result):
            self._won = True

        self._num_guesses += 1
        return result

    def won(self):
        return self._won

    def num_guesses(self):
        return self._num_guesses

    def admit_defeat(self):
        self.lost = True
        return "".join(self.answer)
