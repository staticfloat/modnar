#!/usr/bin/env python

import itertools

def check(vals, word1, word2, word3):
	def get(char):
		if char in vals:
			return vals[char]
		return 0

	num1 = sum([get(word1[idx])*10**(len(word1) - idx - 1) for idx in range(len(word1))])
	num2 = sum([get(word2[idx])*10**(len(word2) - idx - 1) for idx in range(len(word2))])
	num3 = sum([get(word3[idx])*10**(len(word3) - idx - 1) for idx in range(len(word3))])

	if num1 + num2 == num3:
		print "HOLY CRAP WE GOT IT"
		return True
	return False



def do1():
	word1 = 'knife'
	word2 = 'lion'
	word3 = 'horses'

	vals = {'n':8}
	for numbers in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 9]):
		vals['e'] = numbers[0]
		vals['k'] = numbers[1]
		vals['r'] = numbers[2]
		vals['f'] = numbers[3]
		vals['l'] = numbers[4]
		vals['s'] = numbers[5]
		vals['h'] = numbers[6]
		vals['i'] = numbers[7]
		vals['o'] = numbers[8]

		if check(vals, word1, word2, word3):
			print "GOT 'EM COACH!"
			print vals
			return
	print "I couldn't do it. :("

do1()