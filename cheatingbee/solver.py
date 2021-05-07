class Solver:

    @staticmethod
    def solve(required_letters, optional_letters, word_dict):
        required_letters = set(required_letters)
        optional_letters = set(optional_letters)
        all_letters = optional_letters.union(required_letters)
        answers = []
        for word in word_dict:
            if required_letters.issubset(word_dict[word]):
                if word_dict[word].issubset(all_letters):
                    answers.append(word)
        return answers
