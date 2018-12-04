#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 2, challenge 1
https://adventofcode.com/2018/day/2

- Scan the input file
- Find the strings which defers from one another by exactly one letter (at the same index)
- Return the string without the letter that is different
"""

import os
from itertools import combinations

INPUT_FILENAME = 'input.txt'

def main():
	strings = list()
	try:
		file = os.path.join(os.getcwd(), INPUT_FILENAME)
		with open(file) as f:
			strings = list(string.strip() for string in f)
		pairs = list(combinations(strings, 2))
		for pair in pairs:
			diffs = [i for i in range(len(pair[0])) if pair[0][i] != pair[1][i]]
			if len(diffs) == 1:
				print('{}{}'.format(pair[0][:diffs[0]], pair[0][diffs[0]+1:]))
				exit()

	except Exception as e:
		raise e


if __name__ == '__main__':
	main()