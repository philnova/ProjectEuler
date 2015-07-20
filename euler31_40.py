import time
import math
import itertools

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

#print money_count_dynamic()

#======================================#

"""
Problem 32:

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
	return len(c) == 9 and len(set(c)) == 9 and not '0' in c

def find_all_pandigital():
	alim = 9999
	blim = 999
	total = []
	for a in xrange(alim):
		for b in xrange(blim):
			if is_product_pandigital(a,b):
				total.append((a*b))
				print a, b, a*b
	return sum(list(set(total)))

#print find_all_pandigital()

#======================================#

"""
Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def do_digits_cancel(numerator, denominator):
	num_list, denom_list = list(str(numerator)), list(str(denominator))
	for digit in num_list:
		if digit in denom_list and digit != "0":
			new_num = [i for i in num_list]
			new_num.remove(digit)
			new_denom = [i for i in denom_list]
			new_denom.remove(digit)
			if  not float(new_denom[0]) == 0.0 and float(numerator) / denominator == float(new_num[0]) / float(new_denom[0]):
				return True
	return False

def find_all_cancelable():
	all_cancelable = []
	for n in xrange(10,100):
		for d in xrange(10,100):
			if n!=d and float(n)/d < 1 and do_digits_cancel(n,d):
				all_cancelable.append((n,d))

	common_num, common_denom = 1,1
	for n, d in all_cancelable:
		common_num*=n
		common_denom*=d
	return common_num, common_denom

#print do_digits_cancel(30,50)
#print do_digits_cancel(30,49)
#print do_digits_cancel(49,98)
#print find_all_cancelable()

#======================================#

"""
Problem 34:

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def is_n_factorial_sum(n):
	digit_list = list(str(n))
	return sum([math.factorial(int(i)) for i in digit_list]) == n

def find_all_factorial_sums(limit=100000):
	sum_n = 0
	for n in xrange(3,limit):
		if is_n_factorial_sum(n):
			print n
			sum_n += n
	return sum_n

#print find_all_factorial_sums()

#======================================#

"""
Problem 35:

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def rotate_number(n):
	strnum = list(str(n))
	rotations = []
	for dummy in range(len(strnum)):
		last = strnum.pop()
		strnum = [last] + strnum
		rotations.append(int(''.join(strnum)))
	return rotations

#print rotate_number(1003)

def is_prime(n):
	if n in (0,1):
		return False
	elif n == 2:
		return True
	for i in range(3, n):
		if n % i == 0:
			return False
	return True

def find_circular_primes(lo,hi):
	primes = [2]
	for n in xrange(lo,hi,2):
		if is_prime(n) and all([is_prime(i) for i in rotate_number(n)]):
			print n
			primes.append(n)
	return primes

#print find_circular_primes(3,199999) + find_circular_primes(300001,399999) + find_circular_primes(500001,599999) + find_circular_primes(700001,799999) + find_circular_primes(900001,999999)

#======================================#

"""
Problem 36:

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_n_palindrome(n):
	return n == int(''.join(reversed([i for i in str(n)])))

def is_n_twobase_palindrome(n):
	return is_n_palindrome(n) and is_n_palindrome(int(bin(n)[2:]))

print is_n_palindrome(585)
print is_n_palindrome(1001001001)
print is_n_palindrome(1234)

print is_n_twobase_palindrome(585)

def find_all_twobase_palindrome(limit=1000000):
	total = 0
	for n in xrange(1,limit):
		if is_n_twobase_palindrome(n):
			print n
			total += n
	return total

#print find_all_twobase_palindrome()

#======================================#

"""
Problem 37:

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

ONE_DIGIT_PRIMES = [2, 3, 5, 7]

def is_prime(n):
	"""Input odd numbers only"""
	if n in (0,1):
		return False
	elif n in ONE_DIGIT_PRIMES:
		return True
	for i in range(3, n):
		if n % i == 0:
			return False
	return True

BASE_ELEMENTS = [1,3,7,9]
BASE_STRINGS = ['1','2','3','5','7','9']

def all_length_n_permutations(iterable,length):
	return ["".join(seq) for seq in itertools.product(iterable,repeat=length)]

#print all_length_n_permutations(BASE_STRINGS,3)

def left_truncate(string):
	return string[1::]

def right_truncate(string):
	return string[:-1]

def is_truncateable_prime(n_string):
	n_string_L = ''.join([i for i in n_string])
	n_string_R = ''.join([i for i in n_string])
	while n_string_L and n_string_R:
		#print n_string_L, n_string_R
		#print is_prime(int(n_string_L)), is_prime(int(n_string_R))
		if is_prime(int(n_string_L)) and is_prime(int(n_string_R)):
			n_string_L = left_truncate(n_string_L)
			n_string_R = right_truncate(n_string_R)

		else:
			return False
	return True

#print is_truncateable_prime('111')
#print is_truncateable_prime('37')
#print is_truncateable_prime('39397')
#print is_truncateable_prime('739397')

#print is_prime(3939)


#print left_truncate("abc")
#print right_truncate("abc")

def find_all_truncated_primes(limit=11):
	prime_list = []
	counter = 2
	while not len(prime_list) == limit:
		print counter
		potentials = all_length_n_permutations(BASE_STRINGS,counter)
		for p in potentials:
			if is_truncateable_prime(p):
				prime_list.append(p)
				print p
		counter+=1
	return prime_list, sum(prime_list)

#print find_all_truncated_primes()

#======================================#

"""
Problem 38:

"""

DIGITS = '1 2 3 4 5 6 7 8 9'.split()
print DIGITS

def find_all_pandigital():
	return [i for i in reversed(sorted(["".join(seq) for seq in itertools.permutations(DIGITS,len(DIGITS))]))]

def is_expressable_as_concat(n_string):
	return True

def largest_pandigital_concatenated():
	all_pandigital = find_all_pandigital()
	for pan in all_pandigital:
		if is_expressable_as_concat(pan):
			return pan

print largest_pandigital_concatenated()

