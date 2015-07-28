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

FACE_DICT = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class PokerHand(object):

	def __init__(self, card_list):
		self.cards = card_list #formatted as [5D, 5S, KD, etc.]
		self.suits = len(set([i[-1] for i in self.cards]))
		self.count_cards()
		
	def count_cards(self):
		self.values = []
		for i in self.cards:
			try:
				self.values.append(int(i[0:-1]))
			except:
				self.values.append(FACE_DICT[i[0:-1]]) #if card is face card, convert to numerical value
		self.values = [i for i in sorted(self.values)]

		self.value_to_frequency = {}
		for val in self.values:
			try:
				self.value_to_frequency[val]+=1
			except KeyError:
				self.value_to_frequency[val]=1

		self.frequency_to_value = {}
		for k,v in self.value_to_frequency.iteritems():
			try:
				self.frequency_to_value[v].append(k)
			except KeyError:
				self.frequency_to_value[v] = [k,]

	def has_straight_flush(self):
		return self.has_flush() and self.has_straight()

	def has_four(self):
		if 4 in self.frequency_to_value.keys():
			self.four_val = self.frequency_to_value[4][0]
			self.next_highest = self.frequency_to_value[1] #self.next_highest stores sorted list (hi to lo) of remaining cards
			return True
		return False

	def has_full_house(self):
		if 3 in self.frequency_to_value.keys() and 2 in self.frequency_to_value.keys():
			self.triple = self.frequency_to_value[3][0]
			self.pair = self.frequency_to_value[2][0]
			return True
		return False

	def has_flush(self):
		if self.suits == 1:
			self.highest_value = self.values[-1]
			return True
		else:
			return False

	def has_straight(self):
		for idx in xrange(len(self.values)-1):
			if not self.values[idx] + 1 == self.values[idx+1]: #REMEMBER TO USE NUMERICAL VALUES FOR FACE CARDS
				return False
		self.highest_value = self.values[-1]
		return True 

	def has_three(self):
		if 3 in self.frequency_to_value.keys():
			self.three_val = self.frequency_to_value[3][0]
			self.next_highest = [g for g in reversed(sorted([i for i in self.values if not i==self.three_val]))] #next_highest will be in reversed sorted order, e.g. [2,3]
			return True
		return False

	def has_two_pair(self):
		if 2 in self.frequency_to_value.keys() and len(self.frequency_to_value[2])==2:
			lo, hi = [i for i in sorted(self.frequency_to_value[2])]
			self.higher_pair = hi
			self.lower_pair = lo
			self.next_highest = self.frequency_to_value[1]
			return True
		return False

	def has_pair(self):
		if 2 in self.frequency_to_value.keys():
			self.pair_val = self.frequency_to_value[2][0]
			self.next_highest = [g for g in reversed(sorted([i for i in self.values if not i==self.pair_val]))]
			return True
		return False

	def best(self):
		"""Return a string representing the value of the best hand."""
		if self.has_straight_flush():
			return 9
		elif self.has_four():
			return 8
		elif self.has_full_house():
			return 7
		elif self.has_flush():
			return 6
		elif self.has_straight():
			return 5
		elif self.has_three():
			return 4
		elif self.has_two_pair():
			return 3
		elif self.has_pair():
			return 2
		else:
			return 1

	def compare(self, other):
		"""Return True if self wins the hand. Return False if other wins."""
		if self.best() > other.best():
			return True
		elif self.best() == other.best():
			if self.best() == 9: #straight flush
				return self.highest_value > other.highest_value

			elif self.best() == 8: #four of a kind
				if self.four_val > other.four_val:
					return True
				elif self.four_val < other.four_val:
					return False
				else:
					print "This is an impossible hand, but whatever"
					return self.next_highest[-1] > other.next_highest[-1]

			elif self.best() == 7: #full house
				#first compare trio
				if self.triple > other.triple:
					return True
				elif self.triple < other.triple:
					return False
				else:
					return self.pair > other.pair

			elif self.best() == 6: #flush
				#compare the values
				for idx, item in enumerate(reversed(self.values)): #loop through in forward order
					if item > list(reversed(other.values))[idx]:
						return True
					elif list(reversed(other.values))[idx] > item:
						return False
					else: #values are the same; go to the next one
						pass
				return False

			elif self.best() == 5: #straight
				return self.highest_value > other.highest_value

			elif self.best() == 4: #three of a kind
				if self.three_val > other.three_val:
					return True
				elif self.three_val < other.three_val:
					return False
				else:
					for idx, item in enumerate(self.next_highest):
						if item > other.next_highest[idx]:
							return True
						elif other.next_highest[idx] > item:
							return False
						else:
							pass
					return False

			elif self.best() == 3: #two pairs
				if self.higher_pair > other.higher_pair:
					return True
				elif other.higher_pair > self.higher_pair:
					return False
				elif self.lower_pair > other.lower_pair:
					return True
				elif other.lower_pair > self.lower_pair:
					return False
				else:
					return self.next_highest[0] > other.next_highest[0]

			elif self.best() == 2: #one pair
				if self.pair_val > other.pair_val:
					return True
				elif other.pair_val > self.pair_val:
					return False
				else:
					for idx, item in enumerate(self.next_highest):
						if item > other.next_highest[idx]:
							return True
						elif other.next_highest[idx] > item:
							return False
						else:
							pass
					return False

			else: #MAY NEED TO FIX THIS
				for idx, item in enumerate(reversed(self.values)):
					if item > list(reversed(other.values))[idx]:
						return True
					elif list(reversed(other.values))[idx] > item:
						return False
					else:
						pass
				return False

		else: #other.best() is greater
			return False



#SELF.NEXT_HIGHEST IS ALWAYS A LIST		

#h1 = PokerHand(['5C', '5D', 'AD', '4D', '5D'])
#h2 = PokerHand(['5C', '5D', 'AD', '8D', '5D'])

#h1 = PokerHand(['3D', '2C', '7D', '7D', '7D'])
#h2 = PokerHand(['2D', '4C', '7D', '7D', '7D'])

#h1 = PokerHand(['2D', '4D', '7D', '8D', '10D'])
#h2 = PokerHand(['2D', '3D', '7D', '8D', '10D'])

#h1 = PokerHand(list("5H 5C 6S 7S KD".split()))
#h2 = PokerHand(list("2C 3S 8S 8D TD".split()))

#print h1.best()
#print h2.best()
#print h1.compare(h2)

def parse_hands(filename):
	total_wins = 0
	with open(filename, 'r') as fo:
		for line in fo:
			h1, h2 = PokerHand(line.split()[0:5]), PokerHand(line.split()[5::])
			if h1.compare(h2):
				total_wins += 1
	return total_wins

#print parse_hands('poker.txt')


#======================================#

"""
Problem 55:

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
"""

def is_palindrome(n):
	if len(str(n))==1:
		return False
	return n == int(''.join(reversed([i for i in str(n)])))

def reverse_and_add(n):
	n_rev = int(''.join([i for i in reversed(str(n))]))
	return n+n_rev

def test_lychrel(n, limit=50):
	n_iterations = 0
	while n_iterations < limit:
		n = reverse_and_add(n)
		n_iterations+=1
		if is_palindrome(n):
			return True, n_iterations, n
	return False, limit, n

#print test_lychrel(4994)
#print test_lychrel(349)
#print test_lychrel(9998)
#print test_lychrel(196)
#for i in xrange(10):
#	print i, test_lychrel(i)

def find_lychrel(limit=10000):
	n_lychrel = 0
	for n in xrange(1,limit):
		if not test_lychrel(n)[0]:
			n_lychrel+=1
			print n
	return n_lychrel

#print find_lychrel()

#======================================#


