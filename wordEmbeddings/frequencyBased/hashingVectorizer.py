from sklearn.feature_extraction.text import HashingVectorizer

aList = [
    "This is me",
    "This is my friend",
    "Is this my friend?",
    "This is the other friend",
]

vec = HashingVectorizer(n_features=16,norm=None)
anArray = vec.fit_transform(aList)
print(anArray.shape)
print(anArray.toarray())