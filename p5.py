#!/usr/bin/env python3
#
# Copyright (c) 2013 Matthew Rheaume
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA


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
