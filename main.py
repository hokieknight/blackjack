"""Blackjack"""
import art
import game

def get_bet(balance):
    """Get bet"""
    bet = -1
    while bet < 0 or bet > balance:
        bet = int(input(f"Place Bet (0->{balance}): $"))
    return bet

def print_hand(name, hand, hide_first):
    """display hand"""

    display = "  " + name + ": "
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

def play_hand(bet):
    """play a hand"""
    player_hand = game.deal_hand()
    dealer_hand = game.deal_hand()

    print_hand("Dealer", dealer_hand, True)
    print_hand("Player", player_hand, False)

    player_done = False
    player_lose = False
    while not player_done:
        action = input("(H)it or (S)tand? ").lower()
        if action == "h":
            player_hand.append(game.deal_card())
            print_hand("Player", player_hand, False)
        elif action == "s":
            player_done = True
        if game.hand_total(player_hand) > 21:
            print("BUST.  You Lose!")
            player_done = True
            player_lose = True
            return -bet

    print_hand("Dealer", dealer_hand, False)
    dealer_done = False
    dealer_lose = False
    while not player_lose and not dealer_done:
        if game.hand_total(dealer_hand) < 17:
            dealer_hand.append(game.deal_card())
            print_hand("Dealer", dealer_hand, False)
        else:
            dealer_done = True
        if game.hand_total(dealer_hand) > 21:
            print("Dealer BUST.  You Win!")
            dealer_done = True
            dealer_lose = True
            return bet

    if not player_lose and not dealer_lose:
        if game.hand_total(dealer_hand) > game.hand_total(player_hand):
            print("Dealer Wins!!")
            return -bet
        if game.hand_total(dealer_hand) < game.hand_total(player_hand):
            print("Player Wins!!")
            return bet
        print("Draw!!")
        return 0

def main():
    """main method"""
    print(art.LOGO)

    balance = 200
    play = True
    while play:
        bet = get_bet(balance)
        if bet > 0:
            balance += play_hand(bet)
        else:
            play = False

        if balance <= 0:
            print("You are out of money")
            play = False


    print("Bye")

main()
