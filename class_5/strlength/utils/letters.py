# a function to return the number of letters in each word of a sentence
def letters_in_words(sentence):
    words = sentence.split()
    word_lengths = []
    for word in words:
        word_lengths.append((word, str(len(word))))
    return word_lengths

print(letters_in_words("I am okay"))



