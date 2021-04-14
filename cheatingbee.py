import pickle

"""
SPELLING BEE RULES:

-words must contain 4 or more letters
-words must inclue the center letter
-no obscure words, hyphenated words, or any proper nouns
-no curse words
-letters can be used more than once
"""

centerletter = set(input('Please enter the center letter: ').rstrip().lower())
otherletters = set(input('Please enter the other six letters: ').rstrip().lower())
letters = otherletters.union(centerletter)

word_dict = pickle.load(open("./data/words.pkl", "rb"))

answers = []
for word in word_dict:
    if centerletter.issubset(word_dict[word]):
        if word_dict[word].issubset(letters):
            answers.append(word)

print(answers)
