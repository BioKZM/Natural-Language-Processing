# importing packages
import nltk
from nltk.util import ngrams


def ngram(text:str,n=1):

    # tokenizing sentence and setting list
    nGrams = ngrams(sequence=nltk.word_tokenize(text),n=n)
    aList = [gram for gram in nGrams]

    return aList

print(ngram("This is the worst thing you can do.",2))