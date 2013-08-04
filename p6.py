#!/usr/bin/env python3
#
# Finds the difference between the sum of the squares of the first one hundred
# numbers and the square of the sum.
#
# (c) 2013 Matthew Rheaume

def solve():
	n = 100

	sum_total = 0
	sum_to_n = sum(list(range(1,n+1)))

	for i in range(1,n+1):
		sum_total += i * (sum_to_n - i)

	return sum_total

if __name__ == "__main__":
	print(solve())
