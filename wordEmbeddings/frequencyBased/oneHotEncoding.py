from sklearn.preprocessing import OneHotEncoder
import numpy as np

def oneHotEncoding(data:str):
    

    # setting an encoder
    encoder = OneHotEncoder()

    # transforming data to one-hot encoding
    oneHotEncodedData = encoder.fit_transform(data).toarray()


    return oneHotEncodedData

# defining sample data
data = np.array([['apple'], ['pear'], ['apple'], ['strawberry'], ['pear']])


# printing data
print("Default Data\n")
print(data)
print("\n\nOne-Hot Encoded Data\n")
print(oneHotEncoding(data))
