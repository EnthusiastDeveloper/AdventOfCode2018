#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 3, challenge 2
https://adventofcode.com/2018/day/3

- Scan the input file for all claims
- Find the only claim's ID that is not being overlaped by any other claim
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

		for n,x,y,width,height in inp:
			if numpy.all(fabric[x:x+width, y:y+height] == 1):
				print(n)
				exit()
	except Exception as e:
		raise e


if __name__ == '__main__':
	main()
