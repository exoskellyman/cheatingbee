class Solver:
    """
    A class that solves the New York Times Spelling Bee

    ...

    Methods
    -------
    solve(required_letters, optional_letters, word_dict)
        Gives all answers to the New York Times Spelling Bee using
        the required and optional letters
    """
    @staticmethod
    def solve(required_letters, optional_letters, word_dict):
        """Gives all answers to the New York Times Spelling Bee using
        the required and optional letters

        Parameters
        ----------
        required_letters: set, required
            A set of the letters required in the Spelling Bee answers
        optional_letters: set, required
            A set of the letters optional in the Spelling Bee answers
        word_dict: dictionary, required
            A dictionary containing words as keys and the set of the words
            letters as the value

        Returns
        -------
        set
            A set containing all the words that are valid answers in the word
            dictionary for the required and optional letters
        """
        all_letters = optional_letters.union(required_letters)
        answers = set()
        for word in word_dict:
            if required_letters.issubset(word_dict[word]):
                if word_dict[word].issubset(all_letters):
                    answers.add(word)
        return answers
