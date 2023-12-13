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

    player_done = False
    player_lose = False
    while not player_done:
        action = input("(H)it or (S)tand? ")
        if action == "H":
            player_hand.append(game.deal_card())
            print_hand("Player", player_hand, False)
        elif action == "S":
            player_done = True
        if (game.hand_total(player_hand) > 21):
            print("BUST.  You Lose!")
            player_done = True
            player_lose = True
    
    print_hand("Dealer", dealer_hand, False)
    dealer_done = False
    dealer_lose = False
    while not player_lose and not dealer_done:
        if (game.hand_total(dealer_hand) < 17):
            dealer_hand.append(game.deal_card())
            print_hand("Dealer", dealer_hand, False)
        else:
            dealer_done = True
        if (game.hand_total(dealer_hand) > 21):
            print("Dealer BUST.  You Win!")
            dealer_done = True
            dealer_lose = True

    if not player_lose and not dealer_lose:
        if (game.hand_total(dealer_hand) > game.hand_total(player_hand)):
            print("Dealer Wins!!")
        elif (game.hand_total(dealer_hand) < game.hand_total(player_hand)):
            print("Player Wins!!")
        else:
            print("Draw!!")

main()
