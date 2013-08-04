#!/usr/bin/env python3
#
# Finds the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20.
#
# (c) 2013 Matthew Rheaume

def euler_sieve(n):
	vals = list(range(2, n+1))
	primes = []

	while (len(vals) != 0):
		for i in [vals[0] * j for j in vals]:
			if (i in vals):
				vals.remove(i)

		primes.append(vals.pop(0))

	return primes

def solve():
	n = 20

	primes = euler_sieve(n)
	prod = 1

	for p in primes:
		i = 1
		while (p**i <= n):
			i += 1

		prod *= p**(i-1)

	return prod

if __name__ == "__main__":
	print(solve())
