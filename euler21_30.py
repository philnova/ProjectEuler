import math
import time
import string

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

#print amicables()

#======================================#

"""Problem 22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

alphlist = list(string.ascii_uppercase)
ALPHADICT = {letter : idx+1 for idx, letter in enumerate(alphlist)}

def namescore(name):
	return sum([ALPHADICT[letter] for letter in name])

total = 0
with open("p022_names.txt","r") as fo:
	for line in fo:
		names_list = line.split(',')

cleaned_list = []
for name in names_list:
	cleaned_list.append(name[1:-1])
cleaned_list.sort()


total = 0
for idx, name in enumerate(cleaned_list):
	total += (idx+1) * namescore(name)

print total