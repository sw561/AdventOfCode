#!/usr/bin/env python

# We are working out buttons on a keypad:
#	1 2 3
#	4 5 6
#	7 8 9
#
# For each line, start at previous button (5 initially) and move around the
# keypad as per the instructions, but without ever leaving the pad. The final
# position corresponds to the key which is to be pressed.

class Keypad(object):
	def __init__(self):
		self.position = [1,1]

	def move(self, direction):
		if direction=="U":
			self.position[1] -= 1
		elif direction=="D":
			self.position[1] += 1

		elif direction=="R":
			self.position[0] += 1
		elif direction=="L":
			self.position[0] -= 1

		for elem in [0,1]:
			if self.position[elem]<0:
				self.position[elem] = 0
			elif self.position[elem]>2:
				self.position[elem] = 2

	def value(self):
		return self.position[0] + 3*self.position[1] + 1

class Funky_Keypad(object):
	# This has the shape:
	#					sum         pos[0]-pos[1]
	#	    1			0 1 2 3 4	0 1 2 3 4
	#	  2 3 4			1 2 3 4 5     0 1 2 3
	#	5 6 7 8 9		2 3 4 5 6   -2  0 1 2
	#	  A B C			3 4 5 6 7     -2
	#	    D			4 5 6 7 8       -2

	def __init__(self):
		self.position = [0, 2]

	def move(self, direction):
		# Use s and d to find boundary points and know when not to move
		s = sum(self.position)
		d = self.position[0] - self.position[1]

		if direction=="U":
			if s==2 or d==2:
				return
			self.position[1] -= 1
		elif direction=="D":
			if s==6 or d==-2:
				return
			self.position[1] += 1

		elif direction=="R":
			if s==6 or d==2:
				return
			self.position[0] += 1

		elif direction=="L":
			if s==2 or d==-2:
				return
			self.position[0] -= 1

	def value(self):
		if self.position[1]==0:
			return 1
		elif self.position[1]==1:
			return 1 + self.position[0]
		elif self.position[1]==2:
			return 5 + self.position[0]
		elif self.position[1]==3:
			return [None, 'A', 'B', 'C'][self.position[0]]
		elif self.position[1]==4:
			return 'D'

if __name__=="__main__":
	pad = Keypad()
	pad2 = Funky_Keypad()
	pad_code = ""
	pad2_code = ""
	while True:
		try:
			x = raw_input()
		except EOFError:
			break
		for d in x:
			pad.move(d)
			pad2.move(d)
			# print d,"moved to",pad2.position
		pad_code += str(pad.value())
		pad2_code += str(pad2.value())
	print pad_code
	print pad2_code
