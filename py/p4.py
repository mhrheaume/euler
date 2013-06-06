#!/usr/bin/env python
#
# Finds the largest palindrome made from the project of two 3-digit numbers.
#
# (c) 2013 Matthew Rheaume

def is_palindrome(v):
	v_str = str(v)

	i = 0
	j = len(v_str) - 1

	while (i < j):
		if (v_str[i] != v_str[j]):
			return False

		i += 1
		j -= 1
	return True

def solve():
	max_prod = 0

	for i in xrange(99, 999):
		for j in xrange(i, 100, -1):
			prod = i * j

			if (is_palindrome(prod) and prod > max_prod):
				max_prod = prod

	return max_prod

if __name__ == "__main__":
	print solve()
