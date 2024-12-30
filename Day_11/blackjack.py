import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
comp_cards = []

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "draw"
    elif comp_score == 0:
        return "lose, opp blackjack"
    elif user_score == 0:
        return "win, blackjack"
    elif user_score > 21:
        return "lose, you crossed"
    elif comp_score > 21:
        return "win, opp crossed"
    elif user_score > comp_score:
        return "you win"
    else:
        return "you lose"

for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())
    
user_score = calc_score(user_cards)
comp_score = calc_score(comp_cards)

is_game_over = False

while not is_game_over:
    print(f"Your cards: {user_cards}, Your score: {user_score}")
    print(f"Comp cards: {comp_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_deal = input("Type y to get another card: ")
        if user_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
    
    user_score = calc_score(user_cards)

while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calc_score(comp_cards)

# Display the result
result = compare(user_score, comp_score)
print(f"Your final score: {user_score}")
print(f"Comp's final score: {comp_score}")
print(result)
