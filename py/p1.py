#!/usr/bin/env python
#
# Finds the sum of all the multiples of 3 or 5 below 1000
# (c) 2013 Matthew Rheaume

def solve():
	return sum([v for v in range(1,1000) if (v % 3 == 0) or (v % 5 == 0)])

if __name__ == "__main__":
	print solve()
