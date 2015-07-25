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

def n_replace(string, digits_to_replace,digit):
	"""Given str string and int digits_to_replace, replace digits_to_replace characters in string
	with the same digit from the list DIGITS."""
	assert digits_to_replace<=len(string)
	possible_positions = [i for i in itertools.combinations(xrange(len(string)),digits_to_replace)]
	strings = []
	for poss in possible_positions:
			nustring = string[:]
			for p in poss:
				nustring=nustring[0:p]+digit+nustring[p+1::] 
			strings.append(nustring)
	return list(set(strings))

#print len(n_replace("11111", 3))
#expect 100 (10 possible positionings for 3 replacements; 10 digits); output was 100


def find_smallest_switchable_prime(prime_target=6):
	n = 11
	while True:
		if is_prime(n):
			for l in xrange(1,len(str(n))):
				print l
				possible_prime_strings = []
				prime_sum = 0
				for digit in DIGITS:
					possible_prime_strings += [int(i) for i in n_replace(str(n),l,digit)]
					print possible_prime_strings
					prime_sum += sum([int(is_prime(i)) for i in possible_prime_strings])
				if sum(possible_prime_strings) >= prime_target:
						return n
		n += 2
		print n

print find_smallest_switchable_prime()


