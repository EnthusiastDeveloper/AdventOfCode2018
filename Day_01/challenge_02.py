#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 1, challenge 2
https://adventofcode.com/2018/day/1

Go over a list of numbers (positive and negative) and sum them up.
Once get a result which has already been seen - print it and exit.
If needed - go over the file more than once.
"""
import os

INPUT_FILENAME = 'input.txt'
occurences = set()
output = 0

try:
	file = os.path.join(os.getcwd(), INPUT_FILENAME)
	while True:
		with open(file) as f:
			for line in f:
				num = int(line.strip())
				output += num
				if output in occurences:
					print(output)
					exit()
				else:
					occurences.add(output)
except Exception as e:
	raise e
