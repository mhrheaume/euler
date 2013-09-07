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


def solve():
	max_prime = 1
	num = 600851475143

	while (num != 1):
		for i in range(2,num + 1):
			if (num % i != 0):
				continue

			num = num // i
			if (i > max_prime):
				max_prime = i

			break

	return max_prime

if __name__ == "__main__":
	print(solve())
