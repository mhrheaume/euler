#!/usr/bin/env python
#
# Finds the sum of the even-valued terms of the Fibonacci sequence not
# exceeding four million.
#
# (c) 2013 Matthew Rheaume

def solve():
	a = 0
	b = 1
	total = 0

	while (b < 4000000):
		x = a + b
		if (x % 2 == 0):
			total += x

		a = b
		b = x
	
	return total

if __name__ == "__main__":
	print solve()
