import random

# define the possible responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "Bye-bye!", "See you later!"],
    "default": ["I'm not sure what you mean...", "Can you please rephrase that?"]
}

# define a function to handle the user input and return a response
def response(user_input):
    # remove any punctuation and make the input lowercase
    input = user_input.lower().strip(".,! ")
    
    # check if the input matches any of the responses
    for key in responses.keys():
        if input == key:
            return random.choice(responses[key])
    
    # if no match was found, return a default response
    return random.choice(responses["default"])

# testing the chatbot
while True:
    user_input = input(">> ")
    chatbot_output = response(user_input)
    print("Chatbot:", chatbot_output)