"""Game module"""
import random

def deal_card():
    """deal one random card"""
    cards = [["A",11], ["2",2], ["3",3], ["4",4], ["5",5], ["6",6], ["7",7],
            ["8",8], ["9",9], ["10",10], ["J",10], ["Q",10], ["K",10]]
    #return CARDS[random.randint(0, 12)]
    return random.choice(cards)

def deal_hand():
    """deal new hand"""
    new_hand = []
    new_hand.append(deal_card())
    new_hand.append(deal_card())
    return new_hand


def hand_total(hand):
    """Calculate hand total"""
    total = 0
    aces = 0
    for card in hand:
        total += card[1]
        if card[0] == "A":
            aces += 1
    while total > 21 and aces > 0:
        aces -= 1
        total -= 10

    return total
