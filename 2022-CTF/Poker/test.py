from random import getrandbits
from math import prod
import random

HEARTS = "🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾"
SPADES = "🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮"
DIAMONDS = "🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎"
CLUBS = "🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞"
DECK = SPADES+HEARTS+DIAMONDS+CLUBS  # Bridge Ordering of a Deck
ALPHABET52 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop_rstuvw{y}"

CARDS_PER_DEAL = 25
assert CARDS_PER_DEAL % 2 == 1
MAX_DEAL = prod(x for x in range(len(DECK) - CARDS_PER_DEAL + 1, len(DECK) + 1))
DEAL_BITS = MAX_DEAL.bit_length()

random.seed(1234)
