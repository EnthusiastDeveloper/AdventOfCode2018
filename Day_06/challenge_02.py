#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 6, challenge 2
https://adventofcode.com/2018/day/6

- Read the input file which contains the coordinates of points in XY plain.
- Using Manhattan distance algorithm (https://en.wikipedia.org/wiki/Taxicab_geometry)
	calculate the sum of each location's distance from every coordinate.
- Find and return the size of the region formed by all the locations which the sum of
	its distances is less than 10,000
"""

import os

INPUT_FILENAME = 'input.txt'
MAX_DISTANCE = 10000


def main():
	try:
		coordinates = {}
		file = os.path.join(os.getcwd(), INPUT_FILENAME)
		with open(file) as f:
			for index, line in enumerate(f.readlines()):
				xy = line.strip().split(', ')
				coordinates[index] = [int(xy[1]), int(xy[0])]

		region_size = 0
		max_x = max([x for x, _ in coordinates.values()])
		max_y = max([y for _, y in coordinates.values()])

		for i in range(max_x):
			for j in range(max_y):
				if sum(manhattan_distance([i, j], c) for _, c in coordinates.items()) < MAX_DISTANCE:
					region_size += 1
		print(region_size)

	except Exception as e:
		raise e


def manhattan_distance(point_a, point_b):
	try:
		return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
	except ValueError:
		print('Each parameter must have 2 values in it')


if __name__ == '__main__':
	main()
