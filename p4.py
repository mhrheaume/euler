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

	for i in range(99, 999):
		for j in range(i, 100, -1):
			prod = i * j

			if (is_palindrome(prod) and prod > max_prod):
				max_prod = prod

	return max_prod

if __name__ == "__main__":
	print(solve())
