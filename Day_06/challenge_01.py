#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 6, challenge 1
https://adventofcode.com/2018/day/6

- Read the input file which contains the coordinates of points in XY plain.
- Using Manhattan distance algorithm (https://en.wikipedia.org/wiki/Taxicab_geometry)
	calculate the area closest to each of the coordinates.
- Find and return the size of the largest area (by counting the XY coordinates)
"""

import os
import sys

INPUT_FILENAME = 'input.txt'


def main():
	try:
		coordinates = {}
		file = os.path.join(os.getcwd(), INPUT_FILENAME)
		with open(file) as f:
			for index, line in enumerate(f.readlines()):
				xy = line.strip().split(', ')
				coordinates[index] = [int(xy[1]), int(xy[0])]

		grid = init_and_fill_grid(coordinates)
		# print_grid(grid)
		print(get_largest_area(grid, coordinates))

	except Exception as e:
		raise e


def init_and_fill_grid(coordinates):
	max_x = max([x for x, _ in coordinates.values()]) + 1
	max_y = max([y for _, y in coordinates.values()]) + 1
	grid = []
	for i in range(max_y):
		arr = [0] * max_y
		for j in range(max_x):
			arr[j] = closest_to_coordinate([i, j], coordinates)
		grid.insert(i, arr)

	return grid


def manhattan_distance(point_a, point_b):
	try:
		return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
	except ValueError:
		print('Each parameter must have 2 values in it')


def closest_to_coordinate(point, coordinates):
	controlled_by = '.'
	min_distance = sys.maxsize
	for k, v in coordinates.items():
		dist = manhattan_distance(point, v)
		if dist == 0:
			return k
		if dist < min_distance:
			min_distance = dist
			controlled_by = k
		elif dist == min_distance:
			controlled_by = '.'
	return controlled_by


def print_grid(grid):
	for row in range(len(grid)):
		print(''.join(str(grid[row])))


def get_largest_area(grid, coordinates):
	# Since the grid spans to infinity - the areas which are bordering with the grid's edges will be ignored
	disqualified = set()
	for i in range(len(grid)):
		# Add first row
		disqualified.add(grid[0][i])
		# Add first column
		disqualified.add(grid[i][0])
		# Add last row
		disqualified.add(grid[len(grid)-1][i])
		# Add last column
		disqualified.add(grid[i][len(grid)-1])
	disqualified.remove('.')

	largest_area_size = 0
	for coord in coordinates.keys():
		if coord in disqualified:
			continue
		counter = sum(x.count(coord) for x in grid)
		if counter > largest_area_size:
			largest_area_size = counter
	return largest_area_size


if __name__ == '__main__':
	main()
