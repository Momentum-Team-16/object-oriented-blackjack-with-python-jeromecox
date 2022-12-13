import random
import os


SUITS = ['♣️', '♦️', '♠️', '♥️']
RANKS = ['A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10]
FACE = ['J', 'Q', 'K']


class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f"{self.rank}{self.suit} "


class Deck:
  def __init__(self, suits, ranks):
    self.cards = []
    for suit in suits:
      for rank in ranks:
        new_card = Card(suit, rank)
        self.cards.append(new_card)

  def __str__(self):
    deck_as_string = ""
    for card in self.cards:
      deck_as_string += f"{card} "
    return deck_as_string

  def shuffle(self):
    random.shuffle(self.cards)


class Player:
  def __init__(self):
    self.player_hand = []

  def __str__(self):
    hand_as_string = ""
    for card in self.player_hand:
      hand_as_string += f"{card} "
    return hand_as_string


class Dealer:
  def __init__(self):
    self.player_hand = []

  def __str__(self):
    hand_as_string = ""
    for card in self.player_hand:
      hand_as_string += f"{card} "
    return hand_as_string


class Game:
  def __init__(self):
    self.deck = Deck(SUITS, RANKS)
    self.deck.shuffle()

  def deal_card(self, person):
    dealt_card = self.deck.cards.pop()
    person.player_hand.append(dealt_card)

  # def hand_hide(self):
  #   print(f"\nPlayer1 hand: {player1}")
  #   print(f"Dealer hand: {dealer.player_hand[0]}, __")

  # def hand_show(self):
  #   print(f"\nPlayer1 hand: {player1}")
  #   print(f"Dealer hand: {dealer}")

  def calculate_score(self, person):
    total = 0
    num_ace = 0
    for card in person.player_hand:
      if card.rank in range(2, 11):
        total += card.rank
      elif card.rank in FACE:
        total += 10
      else:
        total += 11
        num_ace += 1
    while num_ace and total > 21:
      total -= 10
      num_ace -= 1
    return total


def play_again():
  replay = input("\nWould you like to play again? y / n: ").lower()
  while replay not in ["y", "n", "yes", "no"]:
    print("\nPlease enter a valid input.")
    replay = input("\nWould you like to play again? y / n: ").lower()

  if replay in ["y", "yes"]:
    play_game()
  else:
    print("\nThanks for playing!")


def play_game():
  os.system('clear')
  print("\n♠️ ♥️ LET'S PLAY BLACKJACK! ♣️ ♦️ ")
  new_game = Game()
  player1 = Player()
  dealer = Dealer()

  # print(new_game.deck)
  while len(player1.player_hand and dealer.player_hand) < 2:
    new_game.deal_card(player1)
    new_game.deal_card(dealer)

  # new_game.hand_hide()
  print(f"\nPlayer1 hand: {player1}")
  print(f"Dealer hand: {dealer.player_hand[0]}, __")

  player1_score = new_game.calculate_score(player1)
  dealer_score = new_game.calculate_score(dealer)

  player1_play = True
  while player1_score < 22 and player1_play:
    player_decision = input("\nDoes Player1 want to hit or stand?\n1: Hit or 2: Stand? ").upper()

    if player_decision in ["1", "H", "HIT"]:
      print("\nPlayer1 hits.")
      new_game.deal_card(player1)
      # new_game.hand_hide()
      print(f"\nPlayer1 hand: {player1}")
      print(f"Dealer hand: {dealer.player_hand[0]}, __")
      player1_score = new_game.calculate_score(player1)

    elif player_decision in ["2", "S", "STAND"]:
      print("\nPlayer1 stands.")
      player1_play = False

    else:
      print("\nNot a valid input")

  if player1_score > 21:
    print("\nPlayer1 busts. House wins.")
  else:
    print("\nThe dealer reveals his card.")
    # new_game.hand_show()
    print(f"\nPlayer1 hand: {player1}")
    print(f"Dealer hand: {dealer}")

    while dealer_score < 17:
      print("\nThe dealer hits.")
      new_game.deal_card(dealer)
      # new_game.hand_show()
      print(f"\nPlayer1 hand: {player1}")
      print(f"Dealer hand: {dealer}")
      dealer_score = new_game.calculate_score(dealer)

    if dealer_score > 21:
      print("\nDealer busts. Congratulations! Player1 wins!")
    elif player1_score > dealer_score:
      print("\nThe dealer stands.")
      print("\nCongratulations! Player1 wins!")
    elif player1_score == dealer_score:
      print("\nThe dealer stands.")
      print("\nWomp womp. It's a tie")
    else:
      print("\nThe dealer stands.")
      print("\nPlayer1 loses. House wins.")

  play_again()


if __name__ == "__main__":
  play_game()
