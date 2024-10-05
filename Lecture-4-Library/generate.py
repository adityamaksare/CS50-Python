
import random

coin = random.choice(["heads", "tails"])
print(coin)

# Generating random number between 1 and 10
number = random.randint(1, 10)
print(number)

# shuffle - shuffles the places in the list
cards = ["jack", "queen", 'king']
random.shuffle(cards)
for card in cards:
    print(card)