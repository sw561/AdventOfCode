#!/usr/bin/env python3

def read(fname):
	with open(fname, 'r') as f:
		containers = [int(line) for line in f]
	return containers

def fill(containers, n):
	def fill_(i, n, chosen):
		# Loop over indices
		for j in range(i, len(containers)):
			if containers[j] < n:
				yield from fill_(j+1, n-containers[j], chosen+[j])
			elif containers[j] == n:
				yield chosen+[j]
			else:
				break

	yield from fill_(0, n, [])

if __name__=="__main__":
	import sys
	containers = sorted(read(sys.argv[1]))
	# print("containers:", containers)

	count = 0

	min_length = None
	count_part_2 = 0
	for i in fill(containers, int(sys.argv[2])):
		# print([containers[j] for j in i])
		count += 1

		if min_length is None or len(i) < min_length:
			min_length = len(i)
			count_part_2 = 1
		elif len(i) == min_length:
			count_part_2 += 1

	print("Part 1:", count)
	print("Part 2:", count_part_2)
