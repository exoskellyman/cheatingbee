import pickle


class WordPickler:

    def __init__(self, filepath):
        self.word_dict = pickle.load(open(filepath, "rb"))

    def savewordsaspickle(self, filepath):
        with open(filepath, "wb") as f:
            pickle.dump(self.word_dict, f)

    def savewordsastext(self, filepath):
        with open(filepath, "w") as f:
            f.write('\n'.join(self.word_dict.keys()))
