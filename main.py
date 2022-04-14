
import random


def dealCard():
    """Function to deal a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


userCard = []
computerCard = []

for _ in range(2):
    userCard.append(dealCard())
    computerCard.append(dealCard())
