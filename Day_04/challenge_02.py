#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 4, challenge 2
https://adventofcode.com/2018/day/4

- Scan the input file which contains guards' IDs and on-duty sleeping patterns
	! The file is not chronologically ordered !
- Find out the guard that is most likely to sleep at a specific minute compared to all the other guards
- Return the guard's ID multiplied by that specific minute
	For example - guard #10 and minute 24 would produce 10*24=240
"""

import os
from collections import defaultdict

INPUT_FILENAME = 'input.txt'

def main():
	data = defaultdict(list)
	try:
		file = os.path.join(os.getcwd(), INPUT_FILENAME)
		with open(file) as f:
			sorted_file = sorted(f.readlines())
		guard_id = ''
		falls_asleep = -1
		wakes_up = -1
		for line in sorted_file:
			line = line.strip().split(' ')
			if line[3][0] == '#':
				# First row in block declares the guard 
				guard_id = line[3][1:]
				# Only declare new array if has not been already declared
				if not data[guard_id]:
					data[guard_id] = [0] * 60
			else:
				action = ' '.join(line[2:])
				if action == 'falls asleep':
					falls_asleep = int(line[1][:-1].split(':')[1])
				if action == 'wakes up':
					wakes_up = int(line[1][:-1].split(':')[1])
					for i in range(falls_asleep, wakes_up):
						data[guard_id][i] += 1
					falls_asleep = -1
					wakes_up = -1

		global_best_shot = 0
		timeframe = 0
		# Find the minute mark which has the highest probability for a sleeping guard
		for guard in data.keys():
			# print(guard, '->', data[guard])
			best_shot = max(data[guard])
			if best_shot > global_best_shot:
				# Save the minute mark
				timeframe = data[guard].index(best_shot)
				# Save the elf's ID number
				guard_id = guard
				# Save the probablity found for future comparisons
				global_best_shot = best_shot

		print(int(guard_id) * int(timeframe))
	except Exception as e:
		raise e


if __name__ == '__main__':
	main()
