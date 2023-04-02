import random

# define the possible responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Hi, how can I assist you today?"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?", "I'm great, thanks for asking!"],
    "what are you doing": ["I'm chatting with you!", "Just hanging out, what about you?", "I'm busy chatting with you!"],
    "who are you": ["I'm a chatbot!", "I'm a simple AI language model designed to chat with you.", "I'm your virtual assistant!"],
    "where are you from": ["I was created by BioKZM for his assingment", "I'm from the digital world.", "I exist in the virtual space."],
    "what can you do": ["I can chat with you, answer your questions, and even tell you jokes!", "I can provide you with information and assistance on a variety of topics."],
    "tell me a joke": ["Why did the tomato turn red? Because it saw the salad dressing!", "What do you call an alligator in a vest? An investigator!", "Why was the math book sad? Because it had too many problems."],
    "what's the weather like": ["I'm sorry, I don't have access to real-time weather data.", "You can check your local weather forecast for more information."],
    "what's your favorite color": ["I don't have a favorite color, I'm just a computer program!", "I don't have personal preferences like humans do, but if I'm going to choose one, It will be red."],
    "what's your favorite food": ["I don't eat food, I'm just a computer program!", "I don't have taste buds like humans do."],
    "what's the meaning of life": ["That's a deep question! Philosophers and scientists have been debating the meaning of life for centuries.", "The meaning of life is subjective and can vary from person to person."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure what you mean...", "Can you please rephrase that?", "I didn't understand, could you please rephrase that?"]
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