import time
import math
import itertools

#======================================#

"""
Problem 51:

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

DIGITS = "0 1 2 3 4 5 6 7 8 9".split()

def is_prime(n):
	if n in (0,1):
		return False
	if n % 2 == 0:
		return False
	for i in range(3, n):
		if n % i == 0:
			return False
	return True

def n_replace(string, digits_to_replace):
	"""Given str string and int digits_to_replace, replace digits_to_replace characters in string
	with the same digit from the list DIGITS."""
	assert digits_to_replace<=len(string)
	possible_positions = [i for i in itertools.combinations(xrange(len(string)),digits_to_replace)]
	return possible_positions

def p():
	strings = []
	for poss in possible_positions:
			nustring = string[:]
			for p in poss:
				nustring=nustring[0:p]+digit+nustring[p+1::] 
			strings.append(nustring)
	return list(set(strings))

#print len(n_replace("11111", 3))
#expect 100 (10 possible positionings for 3 replacements; 10 digits); output was 100


def find_smallest_switchable_prime(prime_target=8):
	n = 120371
	while True:
		if is_prime(n):
			print n
			for l in xrange(1,len(str(n))):
				possible_positions = n_replace(str(n),l)
				for poss in possible_positions:
					potential_primes = []
					for d in DIGITS:
						new_num = str(n)
						for p in poss:
							new_num = new_num[0:p]+d+new_num[p+1::] 
						potential_primes.append(new_num)
					#check number of primes
					potential_primes = [i for i in potential_primes if len(str(int(i)))==len(str(n))]
					prime_bools = [is_prime(int(num)) for num in potential_primes]
					prime_sum = sum([int(is_prime(int(num))) for num in potential_primes])
					if prime_sum>=prime_target:
						return n, potential_primes, prime_bools
				
		n += 2
		#print n

#print is_prime(56003)

#n, p, b = find_smallest_switchable_prime()
#for idx, i in enumerate(p):
#	print i, b[idx]

#print find_smallest_switchable_prime()

#======================================#

"""
Problem 52:

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def digits_in_n(n):
	"""Return a list of digits in integer n"""
	return [i for i in sorted([char for char in str(n)])]

#print digits_in_n(534)
#print digits_in_n(534)==digits_in_n(345)
#print digits_in_n(534)==digits_in_n(344)

def find_n():
	n=1
	while True:
		print n
		test_list = [i * n for i in xrange(2,7)]
		n_digits = digits_in_n(n)
		if all([digits_in_n(i)==n_digits for i in test_list]):
			return n
		n+=1

#print find_n()

#======================================#

"""
Problem 53:

"""

def choose(n,r):
	"""For integers n and r, return number of ways of choosing r items from n."""
	return float(math.factorial(n))/(math.factorial(r) * math.factorial(n-r))

#print choose(5,3)
def does_choosen_exceed_limit(n,limit=1000000):
	total=0
	for r in xrange(n,1,-1):
		if choose(n,r)>limit:
			total+=1
	return total

#total = 0
#for i in xrange(1,101):
#	total+=does_choosen_exceed_limit(i)
#print total

#======================================#

"""
Problem 54:

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

class PokerHand(object):

	def __init__(self, card_list):
		self.cards = card_list
		self.suits = []
		self.values = []

	def has_straight_flush(self):
		return self.has_flush() and self.has_straight()

	def has_four(self):
		pass

	def has_full_house(self):
		pass

	def has_flush(self):
		pass

	def has_straight(self):
		pass

	def has_three(self):
		pass

	def has_two_pair(self):
		pass

	def has_pair(self):
		pass

	def compare(self, other):
		"""Return True if self wins the hand. Return False if other wins."""
		pass
