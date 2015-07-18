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


def money_count_dynamic(target = 10, coinvals = (1, 2, 5, 10, 20, 50, 100, 200)):
	ROUTES_CACHE = {i : 0 for i in xrange(target+1)}
	for c in coinvals:
		if c<=target:
			ROUTES_CACHE[c]=1
	for val in xrange(2,target+1):
		print val
		for c in coinvals:
			if c!=val and val-c in ROUTES_CACHE.keys():
				print val-c
				ROUTES_CACHE[val]+=ROUTES_CACHE[val-c]
	return ROUTES_CACHE

print money_count_dynamic()

