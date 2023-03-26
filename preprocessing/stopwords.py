# importing packages
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



def stopword(text:str):

    

    # we need to tokenize the text before filtering
    tokenizedText = word_tokenize(text)

    # setting up stop words
    stopWords = stopwords.words("english")

    # preparing a list for filtered text
    aList = [word for word in tokenizedText if word.lower() not in stopWords]

    return aList


# random text to be filtered
aText = "I am a man who loves coding."
print(f"Original text: {aText}")
print("Filtered text: {}".format(stopword(aText)))