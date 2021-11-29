#importing modules
import random
from art import logo
from replit import clear

#initializing the card list with its respective BlackJack scores
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#initializing result strings
draw = "It's a DRAW!"
player_bj_win = "You win with a BlackJack!!!"
computer_bj_win = "The Computer wins with a BlackJack :("
player_went_over = "You went over. You Lose :("
computer_went_over = "The Computer went over. You Win!!!"
player_score_greater = "You win by beating the Computer's Score!!!"
computer_score_greater = "The Computer wins by beating your score :("     

#function to draw a random card from the card_list
def draw_card():
  """ Draws a random card and return it"""
  card = random.choice(card_list)
  return card

#function to check sum of a hand of cards
def check_sum(hand):
  """ Take a list of cards, and returns the score"""

  #if the sum is 21, and there are only 2 cards in the hand, the player has a blackjack, and return 0
  if sum(hand) == 21 and len(hand)== 2:
    return 0
  
  #if there is an ace in the hand, and the sum is greater than 21, we use the ace as a 1, instead of 11
  if 11 in hand and sum(hand)>21:
    hand.append(1)
    hand.remove(11)
  
  #returns the sum
  return sum(hand)

#funtion to compare the user's score and the computer's score
def compare(user_score, computer_score):
  """Compares the user and the computer's scores, and return the corresponding string"""
  if user_score == computer_score:
    return draw
  elif user_score == 0:
    return player_bj_win
  elif computer_score == 0:
    return computer_bj_win
  elif user_score>21:
    return player_went_over
  elif computer_score>21:
    return computer_went_over
  elif user_score>computer_score:
    return player_score_greater
  else:
    return computer_score_greater

#driver BlackJack function
def black_jack():
  #initializing empty player and computer hands
  player_hand = []
  computer_hand = []

  #a boolean variable to end the player's game
  is_user_game_end = False

  #a for loop for adding 2 random card in each hand
  for _ in range(2):
    player_hand.append(draw_card())
    computer_hand.append(draw_card())

  
  #printing the initial hand and score of both the players
  if check_sum(player_hand) == 0:
    print(f"\nYour initial hand is: {player_hand}    Score: 21")
  else:
    print(f"\nYour initial hand is: {player_hand}    Score: {check_sum(player_hand)}")
  print(f"The Computer's first card: {computer_hand[0]}\n")

  #a loop which keeps on adding cards to player's hand, until the player's game ends
  while not is_user_game_end:
    #variable to keep a check of the player's hand's sum
    player_sum = check_sum(player_hand)

    #if the player_sum is a blackjack, or is greater than 21
    if player_sum == 0 or player_sum>21:
      is_user_game_end = True
    else:
      #asking the player if he wants to draw another card to his hand
      choice = input("If you want to draw another card, type 'y' else type 'n': ")

      #if yes, then appending a random card to the player's hand
      #else, ending the player's game
      if choice == 'y':
        player_hand.append(draw_card())
        print(f"The new card drawn was: {player_hand[-1]}    Your hand: {player_hand}    Score: {check_sum(player_hand)}")
      elif choice == 'n':
        is_user_game_end = True
    #if the current player's hand's sum is greater than 21, then returning the player_went_over string
    if check_sum(player_hand) > 21:
      return player_went_over
  
  #variable to keep a check of the computer's hand's sum
  computer_sum = check_sum(computer_hand)

  #printing the computer's second card
  print(f"\nThe Compter's second card was: {computer_hand[1]}    Computer's Hand: {computer_hand}    Score: ",end=" ")
  if computer_sum == 0:
    print(21)
  else:
    print(computer_sum)

  #a loop which keeps on adding cards to the computer's hand until the sum is greater than or equal to 17
  while computer_sum!=0 and computer_sum<17:
    computer_hand.append(draw_card())
    computer_sum = check_sum(computer_hand)
    print(f"The Computer drew another card: {computer_hand[-1]}    Computer's Hand: {computer_hand}    Score: {computer_sum}")

  #printing the final hands and their respective scores
  print(f"\nYour final hand: {player_hand}    Computer's final hand: {computer_hand}")
  
  if player_sum == 0 and computer_sum == 0:
    print(f"Your Score: 21    Computer's Score: 21\n")
  elif player_sum == 0:
    print(f"Your Score: 21    Computer's Score: {computer_sum}\n")
  elif computer_sum == 0:
    print(f"Your Score: {player_sum}    Computer's Score: 21\n")
  else:
    print(f"Your Score: {player_sum}    Computer's Score: {computer_sum}\n")

  #comparing the two scores and returning the result
  return compare(player_sum, computer_sum)


#a boolean variable to end the Blackjack game
end_game = False
while not end_game:
  condition = input("\nDo you want to play a game of BlackJack? Type 'yes' or 'no': ").lower()
  clear()
  if condition == "no":
    end_game = True
    print("Thank you!")
  else:
    print(logo)
    print(black_jack())
  