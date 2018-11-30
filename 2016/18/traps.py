#!/usr/bin/env python3

def read(x):
	if x=='^': return True
	return False

def char(x):
	if x: return '^'
	return '.'

def get(row, i):
	if i<0: return False
	if i>=len(row): return False
	return row[i]

def make_map(first_row, n, verbose=True):
	row = list(map(read, first_row))
	new_row = [False]*len(row)

	if verbose:
		print("".join(map(char, row)))

	# Count number of safe squares
	c = sum(1 for i in row if not i)

	for i in range(1,n):
		for j in range(len(row)):
			# New_row is a trap if exactly one of left and right are traps
			new_row[j] = get(row,j-1)!=get(row,j+1)
		# Swap pointers to avoid having to copy or reallocate memory
		row, new_row = new_row, row

		if verbose:
			print("".join(map(char, row)))

		c += sum(1 for i in row if not i)
	return c

print(make_map('..^^.', 3))
print(make_map('.^^.^.^^^^', 10))

f = input()
print(make_map(f, 40))
print(make_map(f, 400000, verbose=False))
