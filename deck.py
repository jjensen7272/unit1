#jacob jensen
#12/18
#deck of cards
import random

deck = []
player1 = []
player2 = []

def makedeck(deck):
    """ populate the deck of cards """

    SUITS = ["hearts", "dimonds", "clubs","spades"]
    VALUES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)


def shuffledeck(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp


def dealcard(deck,player1,player2):
    for i in range(5):
        card = deck.pop(0)
        player1.append(card)
        card = deck.pop(0)
        player2.append(card)
            

makedeck(deck)
print(deck)
print()
shuffledeck(deck)
print(deck)
print()
dealcard(deck,player1,player2)
print()
print(player1)
print(player2)

