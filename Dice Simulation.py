import random

def roll_dice():
    return random.randint(1, 6)

# Simulate rolling a dice 10 times
for _ in range(10):
    result = roll_dice()
    print("The dice rolled:", result)
