import pickle
from pathlib import Path


class WordPickler:
    """
    A class to load and save the word dictionary pickle

    ...

    Attributes
    ----------
    word_dict : dictionary
        a dictionary containing words as keys and the set of the words letters
        as the value

    Methods
    -------
    refine_word_dict(solver_answers, nyt_answers)
        Adds missed answers to the word dictionary and removes invalid answers
        then saves the word dictionary
    """
    DATA_PATH = Path(__file__).resolve().parent.parent / 'data'

    def __init__(self):
        self.word_dict = pickle.load(open(self.DATA_PATH / 'words.pkl', "rb"))

    def refine_word_dict(self, solver_answers, nyt_answers):
        """Adds missed answers to the word dictionary and removes invalid
        answers then saves the word dictionary

        Parameters
        ----------
        solver_answers: set, required
            The answers returned by the solver
        nyt_answers: set, required
            The answers of todays New York Times Spelling Bee
        """
        invalid_answers = solver_answers - nyt_answers
        missed_answers = nyt_answers - solver_answers
        if invalid_answers or missed_answers:
            for invalid in invalid_answers:
                self.word_dict.pop(invalid)
            for missed in missed_answers:
                self.word_dict[missed] = set(missed)
            self.__save()

    def __save(self):
        """Saves the word dictionary in the data directory as words.pkl
        and saves the keys of the word dictionary in words.txt
        """
        with open(self.DATA_PATH / 'words.pkl', "wb") as f:
            pickle.dump(self.word_dict, f)
        with open(self.DATA_PATH / 'words.txt', "w") as f:
            f.write('\n'.join(self.word_dict.keys()))
