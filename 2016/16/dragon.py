#!/usr/bin/env python3

def print_data(disk):
	for k in range(len(disk)):
		if disk[k] is None: break
		print(int(disk[k]), end='')
	print('')

def dragon(data, disk_size):

	disk = [None]*disk_size
	# Copy initial data into disk
	for (i,x) in enumerate(data):
		disk[i] = bool(int(x))
	i += 1

	while i<disk_size:
		disk[i] = 0
		i += 1

		# Copy opposite and reverse of data into next part of data
		j = i-2
		while i<disk_size and j>=0:
			disk[i] = not disk[j]
			i += 1
			j -= 1

		# print_data(disk)

	return disk

def checksum(disk):
	while not len(disk)%2:
		disk = [a==b for a,b in zip(disk[::2], disk[1::2])]
		# print_data(disk)
	return disk

def solve(data, disk_size):
	return checksum(dragon(data, disk_size))

if __name__=="__main__":
	# Example
	x = solve('10000', 20)
	print('---')
	print_data(x)

	# Puzzle
	puzzle_input = '10011111011011001'
	x = solve(puzzle_input, 272)
	print('---')
	print_data(x)

	# Part 2
	x = solve(puzzle_input, 35651584)
	print('---')
	print_data(x)
