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


print count_triangle_words("words42.txt")


