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

from math import sqrt

def divisors(n):
	# 1 and n are both divisors
	count = 2
	i = 2

	while i < (int)(sqrt(n)):
		if n % i == 0:
			# i and n / i are both divisors
			count += 2
		i += 1

	if i * i == n:
		# sqrt(n) is a divisor
		count += 1

	return count


def solve():
	i = 1
	n = 1

	while divisors(n) <= 500:
		i += 1
		n += i

	return n


if __name__ == "__main__":
	print(solve())
