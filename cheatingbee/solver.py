class Solver:

    @staticmethod
    def solve(required_letters, optional_letters, word_dict):
        all_letters = optional_letters.union(required_letters)
        answers = set()
        for word in word_dict:
            if required_letters.issubset(word_dict[word]):
                if word_dict[word].issubset(all_letters):
                    answers.add(word)
        return answers
