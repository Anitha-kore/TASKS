import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# Ask user's name
name = input("Hi! What is your name? ")

if name.lower() == "anitha":
    print("Hello Anitha! Welcome back.")
else:
    print(f"Hello {name}! I'm your AI Chatbot.")

# Define chatbot pairs (patterns and responses)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I'm your friendly AI chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm great! How about you?"]
    ],
    [
        r"what can you do?",
        ["I can chat with you and answer simple questions!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you rephrase it?"]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("\nType something to start chatting with me (type 'bye' to exit):\n")
chatbot.converse()
