from newyorktimes import NewYorkTimes
from wordpickler import WordPickler
from solver import Solver
from twitter import Twitter


def main():
    nyt = NewYorkTimes()
    wp = WordPickler()
    solver_answers = Solver.solve(
        nyt.required_letters, nyt.optional_letters, wp.word_dict
    )
    wp.refine_word_dict(solver_answers, nyt.todays_answers)
    twitter_bot = Twitter()
    twitter_bot.post_tweet(
        list(solver_answers.intersection(nyt.todays_answers)),
        list(nyt.todays_answers),
        list(nyt.todays_pangrams))
