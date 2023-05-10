def letters_in_words(sentence):
    words = sentence.split()
    letter_count = [len(word) for word in words]
    return letter_count


# a function to return the number of words in a sentence
def words_in_sentence(sentence):
    words = sentence.split()
    return len(words)

from .. import strlength