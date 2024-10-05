from collections import Counter
from nltk.metrics import edit_distance
import nltk
nltk.download('brown')
from nltk.corpus import brown

def correct_words(words):
    corpus = Counter(brown.words())

    def correct_word(word, corpus):
        if word in corpus:
            return word
        candidates = sorted(corpus.keys(), key=lambda w: (edit_distance(word, w), -corpus[w]))
        return candidates[0] if candidates else word

    corrected = [correct_word(word, corpus) for word in words]

    return corrected
