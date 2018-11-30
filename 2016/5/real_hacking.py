#!/usr/bin/env python

import hashlib

def mymd5(s, i):
	# Do hashes of leading + index where index is an integer.
	m = hashlib.md5()
	m.update(s+str(i))
	return m.hexdigest()

# PART 1
def find_char(leading):
	# If the first 5 characters are 0, then the sixth character is the next
	# character of the password.
	#
	# Find an 8 character password.
	i = 0
	count = 0
	while count<8:
		h = mymd5(leading, i)
		if h[:5]=="00000":
			print "Found a character",i
			yield h[5]
			count += 1

		i += 1

# PART 2
def find_char_advanced_hacking(leading):
	# Still finding an 8 character password.
	#
	# If the first 5 characters are 0, then the 7th character appears in the
	# password in the position indicated by the 6th character (0-7)
	password = [None]*8

	i = 0
	count = 0
	while count<8:
		h = mymd5(leading, i)
		if h[:5]=="00000":
			print "Found a character",i
			try:
				position = int(h[5])
				if position<8 and password[position] is None:
					print "Using the character"
					password[position] = h[6]
					count += 1
			except ValueError:
				pass

		i += 1

	return "".join(password)

doorID = "abc"

doorID = "ugkcyxxp"

# print "".join(find_char(doorID))

x = "".join(find_char_advanced_hacking(doorID))
print x

with open('output', 'w') as f:
	f.write(x+'\n')
