from puzzle import Puzzle
from solver import Solver


def banner(legend):
    print("#" * (len(legend) + 8))
    print("#   " + legend + "   #")
    print("#" * (len(legend) + 8))


if __name__ == "__main__":
    banner("BEGIN CODE OUTPUT")
    p = Puzzle("hard")
    g = Solver(p)
    g.solve_puzzle()
    for guess in g.get_guesses():
        print(guess)
    print(
        "WIN in " + str(p.num_guesses()) + "!"
        if p.won()
        else "LOSS! It was '" + p.admit_defeat() + "'"
    )
    banner("END CODE OUTPUT")
