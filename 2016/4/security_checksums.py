#!/usr/bin/env python

# Each line consists of a room name (lowercase letters with dashes)
# a sector ID (number) and in square brackets a checksum.
#
# If the checksum consists of the 5 most frequently occuring letters in the
# room name with ties broken alphabetically then the room is real.
#
# Find the sum of the sectorIDs of the real rooms.

# Letters go from 'a' (97) to 'z' (122)
# ord('a')=97, chr(97) = 'a'

letters = [chr(97+i) for i in xrange(26)]

def generate_checksum(room):
	# Work out what we think the checksum should be

	occurrences = [0]*26
	for i in room:
		if i!=' ':
			occurrences[ord(i)-97] += 1

	possible = [x for x in zip(occurrences, letters) if x[0]>0]
	# print possible

	# We need to sort from largest to smallest in terms of frequency
	# but smallest to largest alphabetically

	possible.sort(key=lambda x: (-x[0], x[1]))
	# print "post-sort",possible

	return "".join(x[1] for x in possible[:5])

def is_real(room, checksum):
	expected = generate_checksum(room)
	return expected == checksum

def get_input():
	while True:
		try:
			yield raw_input()
		except EOFError:
			return

def decrypt(room, n):
	# Apply a shift cypher n times where n is the sectorID
	room = list(room)
	for i in xrange(len(room)):
		if room[i]==' ': continue
		x = ord(room[i])-97
		x = (x+n)%26
		room[i] = chr(97+x)

	return "".join(room)

def get_params():
	for s in get_input():
		room = s[:-10].replace('-',' ')
		checksum = s[-6:-1]
		sectorID = int(s[-10:-7])
		yield (room, checksum, sectorID)

if __name__=="__main__":
	# Part 1
	# print sum(sectorID for (room, checksum, sectorID) in get_params()\
	# 		if is_real(room,checksum))

	# Part 2
	for (room, checksum, sectorID) in get_params():
		if is_real(room,checksum):
			print decrypt(room, sectorID), sectorID
