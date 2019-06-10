import sys
import nltk
from nltk.stem.porter import PorterStemmer

def my_stemmer(text):
    ps = PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text

words = []
stemmed_words = []

file = open(sys.argv[1], "r")

for line in file:
    words += nltk.word_tokenize(line)

new_file = open(sys.argv[2], "w")

for word in words:
    new_file.write(my_stemmer(word) + '\n')
