"""Blackjack"""
import art
import game


def print_hand(name, hand, hide_first):
    """display hand"""

    display = name + ": "
    is_first = True
    for card in hand:
        if is_first and hide_first:
            display += "[*]"
            is_first = False
        else:
            display += f"[{card[0]}]"
    if not hide_first:
        display += f" = {game.hand_total(hand)}"
    print(display)


def main():
    """main method"""
    print(art.LOGO)

    player_hand = game.deal_hand()
    dealer_hand = game.deal_hand()

    print_hand("Dealer", dealer_hand, True)
    print_hand("Player", player_hand, False)

    #if input("(H)it or (S)tand? ") == "S":
    print_hand("Dealer", dealer_hand, False)


main()
