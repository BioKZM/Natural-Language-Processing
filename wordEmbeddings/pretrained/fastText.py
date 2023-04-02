import fasttext

def fastText(text:str):

    # loading fast text model
    model = fasttext.load_model('cc.tr.300.bin')

    # classification of the text
    label = model.predict(text)

    # printing output
    print(label[0][0], label[1][0])

# sample text
text = "Bu bir örnek metindir."
fastText(text)

