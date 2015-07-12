#!/usr/bin/env python

z = "tumottowithoutwit"

shift = lambda x, s: chr(((ord(x) - ord('a') + s)%26) + ord('a'))
shift_str = lambda z, s: ''.join([shift(x, s) for x in z])

for i in range(0,26):
	print i, shift_str(z, i)