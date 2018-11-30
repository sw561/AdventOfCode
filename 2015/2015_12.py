#!/usr/bin/env python3

def iterate_dict(u):
	if "red" in u.values():
		return None
	else:
		for key in u:
			if type(u[key]) is dict:
				u[key] = iterate_dict(u[key])
			elif type(u[key]) is list:
				u[key] = iterate_array(u[key])
	return u

def iterate_array(u):
	for i in range(len(u)):
		if type(u[i]) is dict:
			u[i] = iterate_dict(u[i])
		elif type(u[i]) is list:
			u[i] = iterate_array(u[i])
	return u

x = eval(input())

print(iterate_array(x))
