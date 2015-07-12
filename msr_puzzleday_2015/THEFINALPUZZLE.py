#!/usr/bin/env python

#import ipdb
import random

lines = [z.strip() for z in open("fours.txt").read().split('\n')]

def isclose(x, y):
	if sum([int(x[i] == y[i]) for i in range(4)]) == 3:
		return True
	return False


def merge_chains(chains):
	for cidx1 in range(len(chains)):
		for cidx2 in range(len(chains)):
			if cidx1 != cidx2:
				if isclose(chains[cidx1][-1], chains[cidx2][0]):
					chains[cidx1] = chains[cidx1] + chains[cidx2]
					del chains[cidx2]
					return True
				if isclose(chains[cidx1][0], chains[cidx2][-1]):
					chains[cidx2] = chains[cidx2] + chains[cidx1]
					del chains[cidx1]
					merge_chains(chains)
					return True

best_chains = []


for trial in range(100):
	chains = []
	random.shuffle(lines)
	for l in lines:
		chains += [[l]]
		while merge_chains(chains):
			pass

	if len(chains) < len(best_chains) or not len(best_chains):
		best_chains = chains

word = ""
for c in best_chains:
	word += chr(ord('a') + len(c) - 1)
	print chr(ord('a') + len(c) - 1), len(c), c

print
print len(best_chains), word