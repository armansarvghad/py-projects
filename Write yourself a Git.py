import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer"
]

def generate_quote():
    return random.choice(quotes)

print(generate_quote())