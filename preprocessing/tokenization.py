# importing packages
from nltk.tokenize import sent_tokenize, word_tokenize


def sentenceTokenize(text:str):
    # using sent_tokenize to split up some text into sentences
    splitSentence = sent_tokenize(text)
    return splitSentence

def wordTokenize(text:str):
    # splitting word by word
    splitWordByWord = word_tokenize(text)
    return splitWordByWord


aText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget porttitor orci, ut rhoncus ante. Proin fermentum blandit viverra."
print("Split sentence : {}".format(sentenceTokenize(aText)))
print("Split sentence : {}".format(wordTokenize(aText)))