
import random


def dealCard():
    """Function to deal a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


userCards = []
computerCards = []
isGameOver = False

for _ in range(2):
    userCards.append(dealCard())
    computerCards.append(dealCard())


userScore = calculateScore(userCards)
computerScore = calculateScore(computerCards)

if userScore == 0 or computerScore == 0 or userScore > 21:
    isGameOver = True
