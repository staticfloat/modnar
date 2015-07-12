#!/usr/bin/env python

import itertools, sys

idxs = [7, 5, 4, 4, 6, 2, 3, 4, 4, 2, 5, 4, 6, 3, 4, 3, 2, 7, 3, 2, 7, 3, 2, 2, 6, 4, 7, 5, 5, 5, 2, 3, 5, 3, 3, 5, 6, 2]

words = [x for x in [z.split('\t')[-1].strip() for z in open("stuff.txt").readlines()] if len(x)]
words.sort()

print words
print idxs
print len(words)
print len(idxs)

done = {}
count = 0

def printit(mapping):
	for idx in range(len(mapping)):
		if mapping[idx] - 1 >= len(words[idx]):
			sys.stdout.write(' ')
		else:
			sys.stdout.write(words[idx][mapping[idx]-1])
	print


known_prefix = [7, 5, 4, 4, 4]

#ridxs = list(idxs[len(known_prefix):])
#ridxs.reverse()
for mapping in itertools.combinations(idxs, len(words)):
	#mapping = list(mapping)
	#mapping.reverse()
	#mapping = tuple(known_prefix + mapping)
	if not mapping in done:
		done[mapping] = True
		printit(mapping)
		#print mapping
		count += 1

	if count > 1000:
		sys.exit(0)



