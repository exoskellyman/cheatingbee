from newyorktimes import NewYorkTimes
from wordpickler import WordPickler
from solver import Solver


def main():
    nyt = NewYorkTimes()
    wp = WordPickler()
    answers = Solver.solve(
        nyt.required_letters, nyt.optional_letters, wp.word_dict
    )
    print(answers)
