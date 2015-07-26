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

print find_smallest_switchable_prime()


