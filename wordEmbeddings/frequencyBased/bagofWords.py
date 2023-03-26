import numpy as np
from nltk.tokenize import word_tokenize

aText = "Half-Life is the best game of all time"
aText2 = "Half-Life is a good game"
aText3 = "Half-Life is great"


aTextList = word_tokenize(aText)
aTextList2 = word_tokenize(aText2)
aTextList3 = word_tokenize(aText3)


aSet = np.union1d(aTextList,aTextList2)
aSet2 = np.union1d(aSet, aTextList3)

print(aSet2)
