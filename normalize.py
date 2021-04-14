import pickle

word_dict = {}

with open("./data/words.txt") as f:
    for line in f:
        word = line.rstrip()
        if '\'' not in word and len(word) >= 4:
            word_set = set(word)
            if len(word_set) <= 7:
                word_dict[word] = set(word)

with open("./data/words.pkl","wb") as f:
    pickle.dump(word_dict,f)
