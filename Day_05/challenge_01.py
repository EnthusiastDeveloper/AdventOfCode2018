#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 5, challenge 1
https://adventofcode.com/2018/day/5

- Read the input file which contains the description of a polymer using 50,000 characters
	The polymer is formed by units, which represented by a single character.
	Units' polarity is represented by capitalization.
		For example - 'A' and 'a' represents the same unit with opposite polarity.
	When Reacting the polymer - any two adjacent units of the same type and reversed polarity are destroyed.
- Scan the polymer compound and return the length of the shortest representation possible
"""

import os

INPUT_FILENAME = 'input.txt'


def main():
	try:
		file = os.path.join(os.getcwd(), INPUT_FILENAME)
		with open(file) as f:
			polymer = f.read().strip()

		letters = list(polymer)
		i = 1
		while i < len(letters):
			if letters[i] == letters[i-1].swapcase():
				del letters[i]
				del letters[i-1]
				i = i-2 if i > 2 else 0
			i += 1

		print(len(letters))

	except Exception as e:
		raise e


if __name__ == '__main__':
	main()
