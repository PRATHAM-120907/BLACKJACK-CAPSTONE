import random

def print_logo():
    print("""
  ____  _            _    _            _    
 |  _ \| |          | |  | |          | |   
 | |_) | | __ _  ___| | _| | __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <| | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\_|\__,_|\___|_|\_\\
    """)

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "🤝 DRAW!"
    elif computer_score == 0:
        return "😞 You lose, opponent has Blackjack!"
    elif user_score == 0:
        return "🎉 You win with a Blackjack!"
    elif user_score > 21:
        return "😵 You went over. You lose!"
    elif computer_score > 21:
        return "😃 Opponent went over. You win!"
    elif user_score > computer_score:
        return "🏆 You win!"
    else:
        return "😢 You lose!"

def print_hand(player, cards, score, reveal_all=True):
    if reveal_all:
        print(f"{player}'s hand: {cards} | Score: {score}")
    else:
        print(f"{player}'s first card: {cards[0]}")

def play_game():
    print_logo()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print_hand("Your", user_cards, user_score)
        print_hand("Computer", computer_cards, computer_score, reveal_all=False)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n--- FINAL HANDS ---")
    print_hand("Your", user_cards, user_score)
    print_hand("Computer", computer_cards, computer_score)
    print("-------------------")
    print(compare(user_score, computer_score))
    print("\n" + "="*40 + "\n")

while input("Do you want to play Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 5)
    play_game()
