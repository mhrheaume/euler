#!/usr/bin/env python
#
# Finds largest prime factor of the number 600851475143
#
# (c) 2013 Matthew Rheaume

def solve():
	max_prime = 1
	num = 600851475143

	while (num != 1):
		for i in xrange(2,num + 1):
			if (num % i != 0):
				continue

			num = num / i
			if (i > max_prime):
				max_prime = i
			break

	return max_prime

if __name__ == "__main__":
	print solve()
