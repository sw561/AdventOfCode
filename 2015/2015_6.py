#!/usr/bin/env python3

import numpy as np

def read(fname):
	data = []
	with open(fname, 'r') as f:
		for line in f:
			u = line.split()
			if u[0]=="turn":
				cmd = u[1]
			else:
				cmd = u[0]
			x1y1 = tuple(int(x)   for x in u[-3].split(','))
			x2y2 = tuple(int(x)+1 for x in u[-1].split(','))
			data.append((cmd, x1y1, x2y2))
	return data

def update(u, cmd):
	(x1, y1), (x2, y2) = cmd[1:]

	if cmd[0]=="toggle":
		u[x1:x2, y1:y2] = 1 - u[x1:x2, y1:y2]
	elif cmd[0]=="off":
		u[x1:x2, y1:y2] = 0
	elif cmd[0]=="on":
		u[x1:x2, y1:y2] = 1
	else:
		raise Exception("{} not understood".format(cmd))

def update_2(u, cmd):
	(x1, y1), (x2, y2) = cmd[1:]

	if cmd[0]=="toggle":
		u[x1:x2, y1:y2] = u[x1:x2, y1:y2] + 2
	elif cmd[0]=="off":
		u[x1:x2, y1:y2] = np.maximum(np.zeros((x2-x1, y2-y1), dtype=int), u[x1:x2, y1:y2] - 1)
	elif cmd[0]=="on":
		u[x1:x2, y1:y2] = u[x1:x2, y1:y2] + 1
	else:
		raise Exception("{} not understood".format(cmd))

if __name__=="__main__":
	import sys

	data = read(sys.argv[1])

	# Part 1
	u = np.zeros((1000, 1000), dtype=int)
	for cmd in data:
		update(u, cmd)
	print(np.sum(u))

	# Part 2
	u = np.zeros((1000, 1000), dtype=int)
	for cmd in data:
		update_2(u, cmd)
	print(np.sum(u))
