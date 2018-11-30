#!/usr/bin/env python

# Each line of input represents the same message but they each line has been
# corrupted by noise.
#
# By finding the most frequently occuring letter in each position of the
# message we can recover the original.

# Letters go from 'a' (97) to 'z' (122)
# ord('a')=97, chr(97) = 'a'

letters = [chr(97+i) for i in xrange(26)]

def get_most_frequent(values):
	# Work out what we think the checksum should be

	occurrences = [0]*26
	for i in values:
		occurrences[ord(i)-97] += 1

	# Part 1
	# (ascii_letter, times) = max(enumerate(occurrences), key=lambda x: x[1])

	# Part 2
	# First filter out letters which never occur
	enum = [x for x in enumerate(occurrences) if x[1]]
	(ascii_letter, times) = min(enum, key=lambda x: x[1])
	return chr(97+ascii_letter)

def get_input():
	messages = []
	while True:
		try:
			messages.append(raw_input())
		except EOFError:
			break
	return messages

if __name__=="__main__":
	messages  = get_input()
	original = []
	for i in xrange(len(messages[0])):
		# For each letter in the message
		new = get_most_frequent([message[i] for message in messages])
		original.append(new)
	print "".join(original)
