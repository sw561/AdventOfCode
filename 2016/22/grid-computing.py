#!/usr/bin/env python3

def get_input():
	while True:
		try:
			q = input().split()
		except EOFError:
			return
		if q[0][0]!='/': continue
		# print(q)
		_,x,y = q[0].split('-')
		x = int(x[1:])
		y = int(y[1:])
		size = int(q[1][:-1])
		used = int(q[2][:-1])
		avai = int(q[3][:-1])
		if size!=used+avai:
			print("JRIUHIQWUFHDIWUEFHIF")
		yield x, y, size, used, avai

class Node(object):
	def __init__(self, x, y, size, used, avai):
		self.x = x
		self.y = y
		self.size = size
		self.used = used
		self.avai = avai

	def __str__(self):
		return "({x},{y}) {size} {used} {avai}".format(**self.__dict__)

	def classify(self):
		# The nodes can be divided into 4 categories
		#   #    used >= 490           these can't be moved
		#   _    avai >   60           empty node
		#   .    64 < used < 75        normal nodes
		if self.used >= 490:
			return ' # '
		elif self.avai >= 60:
			return ' _ '
		elif self.x == 32 and self.y == 0:
			return ' G '
		elif self.x == 0 and self.y == 0:
			return '(.)'
		else:
			return ' . '

def binary_search(nodes, data):
	# Find index corresponding to first node with enough space to hold data
	# Corner cases
	if nodes[0].avai >= data: return 0
	if nodes[-1].avai < data: return len(nodes)

	left = 0 # < data
	right = len(nodes)-1 # >= data
	while right-left>1:
		i = (left+right)//2
		if nodes[i].avai < data:
			left = i
		else:
			right = i
	return right

def number(nodes, data):
	# Find number of nodes with enough space for data
	i_first = binary_search(nodes, data)
	number_fit = len(nodes)-i_first
	return number_fit

def p_nodes(nodes):
	x = -1
	for node in nodes:
		if node.x != x:
			x = node.x
			print('x,y = {:2d},{:1d}'.format(node.x, node.y), end=' ')
		print(node.classify(), end='')
		if node.y == 28:
			print('x,y = {:2d},{:2d}'.format(node.x, node.y))

nodes = [Node(*args) for args in get_input()]

p_nodes(nodes)

# nodes.sort(key=lambda node: node.used, reverse=True)
# for (i,node) in enumerate(nodes): print(i,node)

# Sort by availability
nodes.sort(key=lambda node: node.avai)

# Part 1
n_pairs = 0
for node in nodes:
	if node.used==0: continue
	n_pairs += number(nodes, node.used)
	if node.avai >= node.used:
		n_pairs -= 1 # Since moving data to yourself is silly

print(n_pairs)

# Part 2 number of moves

# Empty node starts at (x,y) = (12, 14)

n_moves = 12 # move to (x,y) = (0, 14)

n_moves += 14 + 31 #   (x,y) = (31, 0)

n_moves += 1 # G is now at (31, 0) and empty node is behind it

# 5 steps to go around and swap with goal data
# do this 31 times to move goal data to (0, 0)
n_moves += 5 * 31

print(n_moves)
