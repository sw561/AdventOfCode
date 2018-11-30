#!/usr/bin/env python

# An lcd screen with pixels numbered from 0 to n where 0,0 is the top left
# corner and (n,0) is the upper right corner, (0,n) is the bottom left corner.
#
# The display can be modified using a series of commands which can
# be:
#
#   # turns on the pixels in a 3 wide two high rectangle in the upper left corner
#	rect 3x2
#
#	# rotates Ath column (counting from left) by B
#	rotate column x=A by B
#
#	# rotates Ath row (counting from top) by B
#	rotate row y=A by B
#
# The screen consists of 50x6 pixels

class Screen(object):
	def __init__(self, cols, rows):
		# Assume number of cols is much larger
		self.rows = rows
		self.cols = cols
		self.data = [[False]*cols for _ in xrange(rows)]

	def show(self):
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				if self.data[row][col]:
					print '#',
				else:
					print ' ',
			print ""
		print "------------------------------"

	def rect(self, width, height):
		for row in xrange(height):
			for col in xrange(width):
				self.data[row][col] = True

	def rotate_col(self, col, n):
		new_col = [False] * self.rows
		for i in xrange(self.rows):
			if self.data[i][col]:
				new_pos = (i+n)%self.rows
				new_col[new_pos] = True

		# Now assign the values from new_col to data
		for i in xrange(self.rows):
			self.data[i][col] = new_col[i]

	def rotate_row(self, row, n):
		n %= self.cols
		shift_index = self.cols-(n%self.cols)

		self.data[row] = self.data[row][shift_index:] +\
			self.data[row][:shift_index]

	def process_instruction(self, line):
		print line
		words = line.split()

		if words[0]=="rect":
			width, height = map(int, words[1].split('x'))
			print "rect",width,height
			self.rect(width, height)

		elif words[0]=="rotate":
			index = int(words[2][2:])
			n = int(words[4])
			if words[1]=="row":
				print "row",index,n
				self.rotate_row(index, n)
			elif words[1]=="column":
				print "col",index,n
				self.rotate_col(index, n)

		else:
			print "QIWEUhqiwufhqiweuh"
		print "-------"

	def count(self):
		return sum(sum(row) for row in self.data)

def get_input():
	while True:
		try:
			yield raw_input()
		except EOFError:
			return

if __name__=="__main__":

	# For the sample need a smaller screen
	# screen = Screen(7, 3)

	screen = Screen(50, 6)

	# Apply the instructions
	for line in get_input():
		screen.process_instruction(line)
		screen.show()

	screen.show()

	# Part 1) how many pixels are lit after following the instructions
	print screen.count()
