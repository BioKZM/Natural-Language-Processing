from sklearn.feature_extraction.text import TfidfVectorizer

aList = [
    "This is me",
    "This is my friend",
    "Is this my friend?",
    "This is the other friend",
]

vec = TfidfVectorizer()

anArray = vec.fit_transform(aList)
print(vec.get_feature_names_out())
print(anArray.shape)
print(anArray.toarray())