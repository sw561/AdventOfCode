#!/usr/bin/env python3

# Given a list of ranges of blocked IPs of the form a-b
# Find the lowest IP address which is not blocked

def get_input():
	while True:
		try:
			a, b = map(int, input().split('-'))
		except EOFError:
			return
		yield a,b

ranges = [x for x in get_input()]

ranges.sort()

def find_lowest(ranges):
	candidate = 0
	for (a,b) in ranges:
		if b<candidate:
			continue
		elif a>candidate:
			return candidate
		elif a<=candidate and b>=candidate:
			candidate = b+1
	return candidate

def count_valid(ranges, max_val):
	count = 0
	candidate = 0
	for (a,b) in ranges:
		if b<candidate:
			continue
		elif a>candidate:
			count += a-candidate
			candidate = b+1
		elif a<=candidate and b>=candidate:
			candidate = b+1
	return count+max_val-candidate+1 # +1 since max_val is included

# print(ranges)
print(find_lowest(ranges))

LARGE_INT = 4294967295
print(count_valid(ranges, LARGE_INT))
