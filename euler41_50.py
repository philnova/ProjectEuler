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

#print largest_pandigital_prime()

#======================================#

"""
Problem 42:

The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

def gen_triangle_number():
	n = 1
	while True:
		tri = (n*(n+1))/2
		yield tri
		n+=1

def triangle_range(limit):
	g = gen_triangle_number()
	triangle_nums=[]
	for dummy in range(limit):
		triangle_nums.append(g.next())
	return triangle_nums

ALPHABET = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

def wordscore(word):
	return sum([ALPHABET.index(char)+1 for char in word])

def count_triangle_words(wordfile):
	word_list = []
	with open(wordfile,'r') as fo:
		for line in fo:
			word_list = [i[1:-1] for i in line.split(",")]
	
	triangles = triangle_range(300)

	counter = 0
	for word in word_list:
		#print word
		if wordscore(word) in triangles:
			print word, wordscore(word)
			counter += 1
	return counter


#print count_triangle_words("words42.txt")

#======================================#

"""
Problem 43:

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

"""

DIGITS = "1 2 3 4 5 6 7 8 9 0".split()

def gen_pandigitals(n_digits):
	return [i for i in reversed(sorted(["".join(seq) for seq in itertools.permutations(DIGITS[0:n_digits])]))]

def check_property(digit_string):
	if int(digit_string[1:4])%2==0:
		if int(digit_string[2:5])%3==0:
			if int(digit_string[3:6])%5==0:
				if int(digit_string[4:7])%7==0:
					if int(digit_string[5:8])%11==0:
						if int(digit_string[6:9])%13==0:
							if int(digit_string[7:10])%17==0:
								return int(digit_string)
	return 0

#print check_property('1406357289')
#print check_property('1406357288')

def find_sum_of_pandigital_with_property():
	total = 0
	pandigitals = gen_pandigitals(10)
	for pan in pandigitals:
		print pan
		total += check_property(pan)
	return total

print find_sum_of_pandigital_with_property()
