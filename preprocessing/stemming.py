# importing packages
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize


def stem(text:str,language:str="english"):

    # setting up the stemmer English
    stem = SnowballStemmer(language=language)


    # we need to tokenize the quote before stemming
    aList = word_tokenize(text)
    stemmedList = [stem.stem(word) for word in aList]
    # print(f"Stemming: {stemmedList}")
    return stemmedList



# a quote from the game Dying Light
aText = "Spike, what's going on? The whole district is down!"

print("Stemming: {}".format(stem(aText)))