import pickle
from pathlib import Path


class WordPickler:
    DATA_PATH = Path(__file__).resolve().parent.parent / 'data'

    def __init__(self):
        self.word_dict = pickle.load(open(self.DATA_PATH / 'words.pkl', "rb"))

    def refine_word_dict(self, solver_answers, nyt_answers):
        invalid_answers = solver_answers - nyt_answers
        missed_answers = nyt_answers - solver_answers
        for invalid in invalid_answers:
            self.word_dict.pop(invalid)
        for missed in missed_answers:
            self.word_dict[missed] = set(missed)
        self.__save()

    def __save(self):
        with open(self.DATA_PATH / 'words.pkl', "wb") as f:
            pickle.dump(self.word_dict, f)
        with open(self.DATA_PATH / 'words.txt', "w") as f:
            f.write('\n'.join(self.word_dict.keys()))
