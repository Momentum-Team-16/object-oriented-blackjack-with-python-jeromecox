import random
import os
import time


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
    self.score = 0

  def __str__(self):
    hand_as_string = ""
    for card in self.player_hand:
      hand_as_string += f"{card} "
    return hand_as_string


class Dealer:
  def __init__(self):
    self.player_hand = []
    self.score = 0

  def __str__(self):
    hand_as_string = ""
    for card in self.player_hand:
      hand_as_string += f"{card} "
    return hand_as_string


class Game:
  def __init__(self):
    self.deck = Deck(SUITS, RANKS)
    self.deck.shuffle()
    self.player1 = Player()
    self.dealer = Dealer()

  def deal_card(self, person):
    dealt_card = self.deck.cards.pop()
    person.player_hand.append(dealt_card)
    self.calculate_score(person)

  def hand_hide(self):
    print(f"\nPlayer1 hand: {self.player1}")
    print(f"Dealer hand: {self.dealer.player_hand[0]}, __")

  def hand_show(self):
    print(f"\nPlayer1 hand: {self.player1}")
    print(f"Dealer hand: {self.dealer}")

  def calculate_score(self, person):
    person.score = 0
    num_ace = 0
    for card in person.player_hand:
      if card.rank in range(2, 11):
        person.score += card.rank
      elif card.rank in FACE:
        person.score += 10
      else:
        person.score += 11
        num_ace += 1
    while num_ace and person.score > 21:
      person.score -= 10
      num_ace -= 1


def play_again():
  replay = input("\nWould you like to play again? y / n: ").lower()
  while replay not in ["y", "n", "yes", "no"]:
    print("\nPlease enter a valid input.")
    replay = input("\nWould you like to play again? y / n: ").lower()

  if replay in ["y", "yes"]:
    play_game()
  else:
    print("\nThanks for playing!")
    os.system('clear')


def sleep_clear(num):
  time.sleep(num)
  os.system('clear')


def play_game():
  os.system('clear')
  print("\n♠️ ♥️ LET'S PLAY BLACKJACK! ♣️ ♦️ ")
  new_game = Game()

  while len(new_game.player1.player_hand and new_game.dealer.player_hand) < 2:
    new_game.deal_card(new_game.player1)
    new_game.deal_card(new_game.dealer)

  new_game.hand_hide()

  player1_play = True
  while new_game.player1.score < 22 and player1_play:
    player_decision = input("\nDoes Player1 want to hit or stand?\n1: Hit or 2: Stand? ").upper()

    if player_decision in ["1", "H", "HIT"]:
      sleep_clear(1)
      print("\nPlayer1 hits.")
      new_game.deal_card(new_game.player1)
      new_game.hand_hide()

    elif player_decision in ["2", "S", "STAND"]:
      print("\nPlayer1 stands.")
      player1_play = False

    else:
      print("\nNot a valid input")

  if new_game.player1.score > 21:
    print("\nPlayer1 busts. House wins.")
  else:
    sleep_clear(2)
    print("\nThe dealer reveals his card.")
    new_game.hand_show()

    while new_game.dealer.score < 17:
      sleep_clear(2)
      print("\nThe dealer hits.")
      new_game.deal_card(new_game.dealer)
      print(new_game.dealer.score)
      breakpoint()
      new_game.hand_show()

    if new_game.dealer.score > 21:
      sleep_clear(2)
      print("\nDealer busts. Congratulations! Player1 wins!")
    elif new_game.player1.score > new_game.dealer.score:
      time.sleep(2)
      print("\nThe dealer stands.")
      time.sleep(2)
      print("\nCongratulations! Player1 wins!")
    elif new_game.player1.score == new_game.dealer.score:
      time.sleep(2)
      print("\nThe dealer stands.")
      time.sleep(2)
      print("\nWomp womp. It's a tie")
    else:
      time.sleep(2)
      print("\nThe dealer stands.")
      time.sleep(2)
      print("\nPlayer1 loses. House wins.")

  time.sleep(1)
  play_again()


if __name__ == "__main__":
  play_game()
