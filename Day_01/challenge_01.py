#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 1, challenge 1
https://adventofcode.com/2018/day/1

Go over a list of numbers (positive and negative), sum them up and print the result
"""

import os

INPUT_FILENAME = 'input.txt'

output = 0
try:
	file = os.path.join(os.getcwd(), INPUT_FILENAME)
	print(sum(int(line.strip()) for line in open(file).readlines()))
except Exception as e:
	raise e
