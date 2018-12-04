#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 3, challenge 1
https://adventofcode.com/2018/day/3

- Scan the input file for all claims
- Find how many square inches of fabric are being used for two or more claims
"""

import os
import re
import numpy

SIZE = 1001
INPUT_FILENAME = 'input.txt'

def main():
	fabric = numpy.zeros((SIZE,SIZE), dtype=numpy.int)
	inp = []
	try:
		file = os.path.join(os.getcwd(), INPUT_FILENAME)
		for line in open(file):
			a = re.split('[^0-9]+', line[1:].strip())
			inp.append([int(d) for d in a])
		for n,x,y,width,height in inp:
			fabric[x:x+width, y:y+height] += 1
		print(numpy.sum(fabric > 1))
	except Exception as e:
		raise e


if __name__ == '__main__':
	main()