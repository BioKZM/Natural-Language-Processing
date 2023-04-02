import re

def cleaning(text:str):
    # removing html tags
    aText = re.sub(r'<.*?>', '', text)
    
    # removing emojis
    emojiList = re.compile("["
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F300-\U0001F5FF"  
                               u"\U0001F680-\U0001F6FF"  
                               u"\U0001F1E0-\U0001F1FF"  
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    aText = emojiList.sub(r'', aText)
    
    # removing urls
    aText = re.sub(r'http\S+', '', aText)
    
    # removing multiple spaces
    aText = re.sub(r'\s+', ' ', aText)
    
    # lowering text for better understanding
    aText = aText.lower()
    
    return aText



aText = """  <div class="content">
                <h1>Hello, world!</h1>
                <p>This is an example text with <strong>HTML tags</strong>, <a href="https://github.com/BioKZM">links</a>, and emojis 😊.</p>
            </div>
       """

print(cleaning(aText))