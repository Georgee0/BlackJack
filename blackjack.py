# black jack 

import random
from replit import clear
from artBJ import logo
 
# function to return a random card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# sum of the cards list
def cal_score(cards):
    # check for blackjack(a hand with 2 cards: an ace + 10) and return 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # check if score is over 21 then remove and replace the ace(11) with ace(1)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack😱"
    elif user_score == 0:
        return "Win, with a Blackjack😎"
    elif user_score > 21:
        return "You went over. You lose😭"
    elif computer_score > 21:
        return "Opponent went over. You win😄"
    elif user_score > computer_score:
        return "You win😄"
    else:
        return "You lose🙁"
        
    
def play_game():
    
    print(logo)
    
    # deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card()) 
        computer_cards.append(deal_card())

    while not is_game_over:
        
        # call the cal_score() to check both user and computer cards
        user_score = cal_score(user_cards)
        computer_score = cal_score(computer_cards)
        print(f'user: card:{user_cards} score:{user_score}')
        print(f'computer: {computer_cards[0]}') 
            
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass.")
            if user_deal == 'y':
                user_cards.append(deal_card)
            else:
                is_game_over == True
                
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = cal_score(computer_cards)
        
    
    print(f"    Your final hand: {user_cards}, final score: {user_score}")    
    print(f"    Computer's hand: {computer_cards}, final score: {computer_score}")    
    print(compare(user_score, computer_score))

#Ask the user if they want to restart the game. If yes, clear the console and
# start a new game and show logo from art.py '''

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()