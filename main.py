############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
from random import choice
from art import logo
#from replit import clear
from os import system
def clear():
    system('clear')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card(cards):
  return choice(cards)  

def show_hand(cards):
  print(cards)

def show_hidden_hand(cards):
  hidden_cards = cards.copy()
  hidden_cards[1] = "X"
  print (hidden_cards)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(hand):
  score = sum(hand)
  #Initial sum
  #for card in hand:
  #  score += card
  #Check for blackjack
  if score == 21 and len(hand) == 2:
    score = 0
  #Check for aces when over 21
  if score > 21:
    for card in hand:
      if card == 11:
        hand.remove(card)
        hand.append(1)
        score -= 10
  return score

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    print ("Tie!")
    result = 0
  elif computer_score == 0:
    print ("Computer blackjack!!!")
    result = -1
  elif user_score == 0:
    print ("Player blackjack!!!")
    result = 1
  elif user_score > 21:
    print("Player busted")
    result = -1
  elif computer_score > 21:
    print("Computer busted")
    result = 1
  elif user_score > computer_score:
    print("Player closer to 21")
    result = 1
  else:
    print("Computer closer to 21")
    result = -1
  return result

def print_winner(result):
  if result == 0:
    print("It's a draw!")
  elif result == 1:
    print("You win!")
  elif result == -1:
    print("You lose!")
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
play_game = "y"
while play_game == "y":
  user_hand = []
  computer_hand = []
  number_initial_cards = 2
  clear()
  print(logo)
  for i in range(number_initial_cards):
    user_hand.append(deal_card(cards))
    computer_hand.append(deal_card(cards))

  end_player = False
  end_computer = False
  score_computer = calculate_score(computer_hand)
  while not end_player:
    score_player = calculate_score(user_hand)


    if score_player == 0 or score_computer == 0 or score_player > 21:
      end_player = True
      end_computer = True

    print("Your hand:")
    show_hand(user_hand)
    print("Computer hand:")
    show_hidden_hand(computer_hand)
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    if not end_player:
      answer = input("Do you want another card (y/n)? ").lower()
      if answer == "y":
        user_hand.append(deal_card(cards))
      else:
        end_player = True

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while not end_computer:
    if score_computer < 17:
      computer_hand.append(deal_card(cards))
      #print(f"Debug, computer hand: {computer_hand}")
      score_computer = calculate_score(computer_hand)
    else:
      end_computer = True

  print("Computer final hand:")
  show_hand(computer_hand)
  print(score_player, score_computer)
  print_winner(compare(score_player, score_computer))
  #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
  play_game = input("Do you want to restart the game (y/n)? ").lower()

