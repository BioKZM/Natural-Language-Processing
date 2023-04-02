from gensim.models import Word2Vec

def word2Vec(aList):

    # Word2Vec modeli eğitimi
    model = Word2Vec(aList, min_count=1)

    # Kelimelerin vektörleri
    print(model.wv['sample'])
    print(model.wv['text'])

# sample text
aList = [['this', 'is', 'a', 'sample', 'text'], ['this', 'is', 'a', 'sample', 'text', 'too']]

# printing results
word2Vec(aList)