import pickle
from pathlib import Path


class WordPickler:
    DATA_PATH = Path(__file__).resolve().parent.parent / 'data'

    def __init__(self):
        self.word_dict = pickle.load(open(self.DATA_PATH / 'words.pkl', "rb"))

    def save_words_as_pickle(self):
        with open(self.DATA_PATH / 'words.pkl', "wb") as f:
            pickle.dump(self.word_dict, f)

    def save_words_as_text(self):
        with open(self.DATA_PATH / 'words.txt', "w") as f:
            f.write('\n'.join(self.word_dict.keys()))
