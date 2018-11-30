#!/usr/bin/env python3

def read(fname):
	reindeer = dict()
	with open(fname, 'r') as f:
		for line in f:
			u = line.split()
			reindeer[u[0]] = tuple(int(u[i]) for i in [3, 6, -2])

	return reindeer

def distance(time, speed, run_time, rest_time):
	unit_time = run_time + rest_time

	distance_per_unit = speed * run_time
	distance = distance_per_unit * (time // unit_time)

	remaining_time = time % unit_time
	distance += min(remaining_time, run_time) * speed

	return distance

if __name__=="__main__":
	import sys
	data = read(sys.argv[1])

	# print("data:", data)

	# Part 1
	farthest = max(distance(int(sys.argv[2]), *data[x]) for x in data)
	print("farthest:", farthest)

	# Part 2
	points = {reindeer: 0 for reindeer in data}
	for time in range(1, int(sys.argv[2])+1):
		farthest = 0
		winners = []
		for x in data:
			c = distance(time, *data[x])
			if c > farthest:
				farthest = c
				winners = [x]
			elif c == farthest:
				winners.append(x)

		for winner in winners:
			points[winner] += 1

	print("points[winner]:", max(points.values()))
