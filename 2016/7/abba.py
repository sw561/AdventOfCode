#!/usr/bin/env python

# A string contains an 'abba' if it contains a sequence of 4 characters which
# are a palindrome, and the outer two characters are different from the inner
# two.
#
# An IP address supports TLS if it contains an abba and the hypernet sequences
# (within square brackets) do NOT contain an abba

def contains_abba(s):
	# Loop over characters which have one to the left and two to the right
	for i in xrange(1, len(s)-2):
		# Middle two characters are equal
		if s[i]==s[i+1]:
			# First and second are different
			if s[i-1]!=s[i]:
				# First and last are equal
				if s[i-1]==s[i+2]:
					return True
	return False

def contains_abba_list(string_list):
	for s in string_list:
		if contains_abba(s):
			return True

	return False

def TLSsupport(normal, hypernet):
	n = contains_abba_list(normal)
	h = contains_abba_list(hypernet)
	# print "Results for normal, hypernet",n,h
	# print "---"
	return n and not h

def get_aba_list(normal_list):
	# Yield all the 'aba's that we find so we can check if the corresponding
	# bab can be found in the hypernet sequence.
	aba_list = []
	for s in normal_list:
		for i in xrange(1, len(s)-1):
			if s[i-1]==s[i+1]:
				if s[i-1]!=s[i]:
					aba_list.append(s[i-1:i+2])
	return aba_list

def check_bab(s, aba_list):
	for i in xrange(1, len(s)-1):
		if s[i-1]==s[i+1] and s[i-1]!=s[i]:
			# We have a possible bab. Now just need to check if it matches any
			# of the aba's that we are looking for.
			for aba in aba_list:
				if s[i-1]==aba[1] and s[i]==aba[0]:
					return True

def check_bab_list(hypernet_list, aba_list):
	for elem in hypernet_list:
		if check_bab(elem, aba_list):
			return True
	return False

def SSLsupport(normal, hypernet):
	aba_list = get_aba_list(normal)
	result = check_bab_list(hypernet, aba_list)
	return result

def separate(IP):
	# Split into a list of normal segments, and a list of hypernet segments
	# print IP

	# We are making the assumption that the first segement is 'normal'
	if IP[0]=='[':
		print "Found an IP which was not as expected"
		print IP
		exit()

	IP = IP.replace(']', '[')
	IP = IP.split('[')
	# print IP

	normal = IP[::2]
	hypernet = IP[1::2]

	return (normal, hypernet)

def get_input():
	while True:
		try:
			yield raw_input()
		except EOFError:
			return

if __name__=="__main__":
	# Part 1
	# Find number of IPs which support TLS
	# print sum(1 for IP in get_input() if TLSsupport(*separate(IP)))
	countTLS = 0
	countSSL = 0
	for IP in get_input():
		(n, h) = separate(IP)
		countTLS += TLSsupport(n, h)
		countSSL += SSLsupport(n, h)
	print "TLS support:",countTLS
	print "SSL support:",countSSL
