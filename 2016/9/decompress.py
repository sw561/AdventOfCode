#!/usr/bin/env python

def process_marker(m):
	# Remove brackets
	m = m[1:-1]
	(nchars, repeats) = map(int, m.split('x'))

	return (nchars, repeats)

def generate_decompressed(f):

	i = 0
	while True:
		# Have reached end of string
		if i>=len(f):
			return

		if f[i]!='(':
			yield f[i]
			i += 1

		elif f[i]=='(':
			# Have found a marker indicating the following segment is repeated
			# First find the end of the marker
			j = i
			while f[j]!=')':
				j += 1

			(nchars, repeats) = process_marker(f[i:j+1])
			start = j+1
			end = start+nchars

			for k in xrange(repeats):
				yield f[start:end]

			i = end

# Part 2
def decompressed_length_format2(f):
	# Only need length no need to generate actual decompressed string
	# However

	i = 0
	count = 0
	while True:
		# Have reached end of string
		if i>=len(f):
			break

		if f[i]!='(':
			count += 1
			i += 1

		elif f[i]=='(':
			# Have found a marker indicating the following segment is repeated
			# First find the end of the marker
			j = i
			while f[j]!=')':
				j += 1

			(nchars, repeats) = process_marker(f[i:j+1])
			start = j+1
			end = start+nchars

			# The subject of the marker needs to itself be decompressed
			count += repeats*decompressed_length_format2(f[start:end])

			i = end

	return count

if __name__=="__main__":

	samples = [
		"ADVENT",
		"A(1x5)BC",
		"(3x3)XYZ",
		"A(2x2)BCD(2x2)EFG",
		"(6x1)(1x3)A",
		"X(8x2)(3x3)ABCY",
		]

	for s in samples:
		print s
		for h in generate_decompressed(s):
			print h,
		print ""
		print "----"

	f = raw_input()

	# Part 1) length of decompressed file
	count = 0
	for h in generate_decompressed(f):
		count += len(h)
	print "ANSWER TO PART 1:",count
	print "------------------------------"

	samples = [
		"(3x3)XYZ",
		"X(8x2)(3x3)ABCY",
		"(27x12)(20x12)(13x14)(7x10)(1x12)A",
		"(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN",
		]

	for s in samples:
		print s, decompressed_length_format2(s)

	x = decompressed_length_format2(f)
	print "ANSWER TO PART 2:",x

	with open("output",'w') as f:
		f.write("%d\n" % x)
