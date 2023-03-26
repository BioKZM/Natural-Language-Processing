from sklearn.feature_extraction.text import CountVectorizer

aList = [
    "This is me",
    "This is my friend",
    "Is this my friend?",
    "This is the other friend",
]

vec = CountVectorizer(ngram_range=(2,2))

anArray = vec.fit_transform(aList)
print(vec.get_feature_names_out())
print(anArray.toarray())