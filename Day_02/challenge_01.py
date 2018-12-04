#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 2, challenge 1
https://adventofcode.com/2018/day/2

- Scan the input file
- Count all strings with a letter apearing exactly twice
- Count all strings with a letter apearing exactly 3 times
- Return the multiplication of the two counters
"""

import os

INPUT_FILENAME = 'input.txt'

def main():
	count_twos = 0
	count_threes = 0
	try:
		file = os.path.join(os.getcwd(), INPUT_FILENAME)
		with open(file) as f:
			for line in f:
				letters = letter_coutner(line.strip())
				if 2 in letters.values():
					count_twos += 1
				if 3 in letters.values():
					count_threes += 1
		print(count_twos * count_threes)

	except Exception as e:
		raise e


def letter_coutner(string):
	counter = {}
	for letter in string:
		if letter in counter:
			counter[letter] += 1
		else:
			counter[letter] = 1
	return counter


if __name__ == '__main__':
	main()