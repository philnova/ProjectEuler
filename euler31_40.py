import time
import math

#======================================#

"""
Problem 31:

In England the currency is made up of pound, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).
It is possible to make 2 in the following way:

1x1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 2 be made using any number of coins?
"""


def money_count_dynamic(target = 200, coinvals = (1, 2, 5, 10, 20, 50, 100, 200)):
	ROUTES_CACHE = [[0 for c in coinvals] for t in xrange(target+1)]
	for row in ROUTES_CACHE:
		row[0] = 1
	ROUTES_CACHE[0] = [1 for c in coinvals]
	for row_idx in range(1,target+1):
		for col_idx in range(1,len(ROUTES_CACHE[row_idx])):
			if 0 <= row_idx - coinvals[col_idx] <= target:
				ROUTES_CACHE[row_idx][col_idx] = ROUTES_CACHE[row_idx][col_idx-1] + ROUTES_CACHE[row_idx - coinvals[col_idx]][col_idx]
			else:
				ROUTES_CACHE[row_idx][col_idx] = ROUTES_CACHE[row_idx][col_idx-1]
	return ROUTES_CACHE

print money_count_dynamic()

#======================================#

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def is_product_pandigital(a,b):
	c = a * b
	a, b, c = list(str(a)), list(str(b)), list(str(c))
	c.extend(a)
	c.extend(b)
	return len(c) == 9 and len(set(c)) == 9

def find_all_pandigital():
	alim = 99999
	blim = 9999
	total = []
	for a in xrange(alim):
		for b in xrange(blim):
			if is_product_pandigital(a,b):
				total.append((a*b))
				print a, b
	return sum(list(set(total)))

print find_all_pandigital()
