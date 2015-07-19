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

