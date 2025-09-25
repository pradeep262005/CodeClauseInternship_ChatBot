import nltk
import random
import string

nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"good morning",
        ["Good Morning!!!,How can I help you?","Good Morning! Have a pleasant day!"]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot.", "You can call me ChatBot!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good, thank you!", "I'm fine. How about you?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! It was nice talking to you."]
    ]
]


chatbot = Chat(pairs, reflections)
print("ChatBot: Hi! Type 'quit' to exit.")
chatbot.converse()
