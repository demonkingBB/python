import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
name = input("What is your name? ")

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    total = sum(hand)
    if total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total

def compare(user_score, computer_score):
    if user_score == 0 and computer_score == 0:
        return "Both have Blackjack! It's a tie!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif computer_score == 0:
        return "Dealer has Blackjack! You lose!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Dealer went over 21. You win!"
    elif user_score == computer_score:
        return "It's a draw/tie!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    # print(logo)

    # 1. Reset hands at the start of each game
    player = []
    dealer = []

    # 2. Deal initial cards
    for _ in range(2):
        player.append(deal_card())
        dealer.append(deal_card())

    is_game_over = False

    # Calculate initial scores
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    # Check if either side got a natural Blackjack immediately
    if player_score == 0 or dealer_score == 0:
        is_game_over = True

    # Player's turn (skipped if someone hit Blackjack)
    while not is_game_over:
        print(f"\nYour cards: {player}, current score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score >= 21:
            is_game_over = True
        else:
            ask = input("Type 'y' to hit, 'n' to stand: ").lower()
            if ask == 'y':
                player.append(deal_card())
                player_score = calculate_score(player)
            else:
                is_game_over = True

    # 4. Dealer's turn (only runs if player didn't bust)
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    if player_score <= 21:
        while dealer_score < 17:
            dealer.append(deal_card())
            dealer_score = calculate_score(dealer)

    # 5. Final results
    print(f"\nYour final hand: {player}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))


# --- MAIN REPLAY LOOP ---
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()

print(f"Thanks for playing, {name}!")