import art
import random

'''RULES:
- The deck is unlimited in size
- There are no jokers
- The Jack/Queen/King all count as 10 (hence the reason there's 4 '10s' in the cards list)
- The Ace can count as 11 or 1.
- The cards in the list have equal probability of being drawn,
- Cards are not removed from the deck as they are drawn,
- The computer is the dealer.'''

def clear_screen():
    print("\n" * 50)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def first_draw(player_hand, current_score_player, computer_hand, current_score_dealer):
    #Getting a hand for the player
    for i in range(2):
        player_hand += [random.choice(cards)]
    current_score_player = sum(player_hand)
    if current_score_player > 21 and 11 in player_hand:
        current_score_player -= 10

    #Getting the hand for the computer
    for i in range(2):
        computer_hand += [random.choice(cards)]
    current_score_dealer = sum(computer_hand)

    return player_hand, current_score_player, computer_hand, current_score_dealer


def dealer_turn(computer_hand, current_score_dealer):
    while current_score_dealer < 17:
        computer_hand.append(random.choice(cards))
        current_score_dealer = sum(computer_hand)
        if current_score_dealer > 21 and 11 in computer_hand:
            current_score_dealer -= 10
    return computer_hand, current_score_dealer


def player_turn(player_hand, current_score_player):
    player_hand.append(random.choice(cards))
    current_score_player = sum(player_hand)
    if current_score_player > 21 and 11 in player_hand:
        current_score_player -= 10
    return player_hand, current_score_player


def compare(player_score, dealer_score):
    if player_score > 21:
        return "You went over! You lose 😭"
    if dealer_score > 21:
        return "Dealer went over! You win 😄"
    if player_score == dealer_score:
        return "It's a draw!"
    if player_score == 21:
        return "Blackjack! You win 🎉"
    if dealer_score == 21:
        return "Dealer has blackjack. You lose 😢"
    if player_score > dealer_score:
        return "You win! 🎉"
    return "You lose 😢"


def blackjack():
    computer_hand = []
    player_hand = []
    current_score_player = 0
    current_score_dealer = 0

    print(art.logo)

    # First draw
    player_hand, current_score_player, computer_hand, current_score_dealer = first_draw(
        player_hand, current_score_player, computer_hand, current_score_dealer)

    print(f"Your cards: {player_hand}, score: {current_score_player}")
    print(f"Dealer's first card: {computer_hand[0]}")

    game_over = False

    # Player turn
    while not game_over:
        if current_score_player == 21:
            print("Blackjack! You instantly win 🎉")
            return

        choice = input("Type 'Y' to get another card, 'N' to pass: ").upper()

        if choice == "Y":
            player_hand, current_score_player = player_turn(player_hand, current_score_player)
            print(f"Your cards: {player_hand}, score: {current_score_player}")

            if current_score_player > 21:
                print(compare(current_score_player, current_score_dealer))
                return

        elif choice == "N":
            # Dealer turn
            computer_hand, current_score_dealer = dealer_turn(computer_hand, current_score_dealer)
            print(f"Dealer's final hand: {computer_hand}, score: {current_score_dealer}")
            print(compare(current_score_player, current_score_dealer))
            game_over = True


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_screen()
    blackjack()
