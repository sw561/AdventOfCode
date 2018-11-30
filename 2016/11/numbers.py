#!/usr/bin/env python3

from missionaries_cannibals import RTG, microchip, NFLOORS

for i in range(NFLOORS**2):
	print(i, RTG(i), microchip(i))
