import time
import math
import itertools

#======================================#

"""
Problem 41:

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

DIGITS = "1 2 3 4 5 6 7 8 9".split()

def gen_pandigitals(n_digits):
	return [i for i in reversed(sorted(["".join(seq) for seq in itertools.permutations(DIGITS[0:n_digits])]))]

def is_prime(n):
	if n in (0,1):
		return False
	if n % 2 == 0:
		return False
	for i in range(3, n):
		if n % i == 0:
			return False
	return True

def largest_pandigital_prime():
	count = len(DIGITS)
	while count:
		pandigitals = gen_pandigitals(count)
		for pan in pandigitals:
			print pan
			if is_prime(int(pan)):
				return pan
		count-=1

print largest_pandigital_prime()