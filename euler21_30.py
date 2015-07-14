import math
import time

#======================================#

"""
Problem 21:

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def properdiv(n):
	divisors = []
	for i in xrange(1,n):
		if n%i == 0:
			divisors.append(i)
	return sum(divisors)

#print properdiv(properdiv(284))
#print properdiv(220)

def amicables(limit=10000):
	amicable_list = []
	for n in xrange(1,limit):
		if not n in amicable_list:
			current = properdiv(n)
			if not current==n and properdiv(current)==n:
				amicable_list.append(n)
				amicable_list.append(current)
	return sum(list(set(amicable_list)))

print amicables()