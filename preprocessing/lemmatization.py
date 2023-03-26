# importing packages
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize



def lemmatizeSingleWord(word:str,pos:str):
    # setting up lemmatizer for lemmatization
    lem = WordNetLemmatizer()

    # single word lemmatization
    lemmatizedWord = lem.lemmatize(word=word,pos=pos)

    return lemmatizedWord

def lemmatize(sentence:str):
    # setting up lemmatizer for lemmatization
    lem = WordNetLemmatizer()
    # sentence lemmatization
    tokenizedWords = word_tokenize(sentence)
    lemmatizedWords = [lem.lemmatize(word) for word in tokenizedWords]
   
    return lemmatizedWords

# aString = "My friends loves parties"


print("Single word lemmatization: {}".format(lemmatizeSingleWord('better','a')))
print("Sentence lemmatization: {}".format(lemmatize('My friends loves parties')))