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
	# It must be the case that c > 1000 // 3 = 333 in order to satisfy
	# the property a < b < c
	for c in range(1000 // 3 + 1, 1000):
		for b in reversed(range(2, c)):
			a = 1000 - c - b
			if a >= b:
				break

			if a**2 + b**2  == c**2:
				return a * b * c

	return -1

if __name__ == "__main__":
	print(solve())
