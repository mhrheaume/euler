#!/usr/bin/env python3
#
# Finds the Pythagorean triplet a, b, c such that a + b + c = 1000,
# and returns the product a * b * c.
#
# (c) 2013 Matthew Rheaume

def solve():
	# It must be the case that c > 1000 // 3 = 333 in order to satisfy
	# the property a < b < c
	for c in range(1000 // 3 + 1, 1000):
		for b in reversed(range(2, c)):
			a = 1000 - c - b
			if a >= b:
				break

			if a**2 + b**2  == c**2:
				return a * b * c

	return -1

if __name__ == "__main__":
	print(solve())
