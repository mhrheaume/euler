#!/usr/bin/env python
#
# Finds the 10,001st prime number.
#
# (c) 2013 Matthew Rheaume

import math

def is_prime(n):
	for i in xrange(2, int(math.sqrt(n)) + 1):
		if (n % i == 0):
			return False

	return True

def solve():
	count = 0
	n = 1

	while (count < 10001):
		n += 1

		if (is_prime(n)):
			count += 1

	return n

if __name__ == "__main__":
	print solve()
