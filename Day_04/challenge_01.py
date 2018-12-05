#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 4, challenge 1
https://adventofcode.com/2018/day/4

- Scan the input file which contains guards' IDs and on-duty sleeping patterns
	! The file is not chronologically ordered !
- Find out the guard that has slept the most during his duties.
- Find out the specific minute in which that guard was asleep in most of his duties
- Return the guard's ID multiplied by that minute
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

		guards_sleeping_data = {}
		for guard in data.keys():
			minutes_asleep = sum(m for m in data[guard])
			guards_sleeping_data[minutes_asleep] = guard
		selected_guard = guards_sleeping_data[max(guards_sleeping_data)]
		selected_time = data[selected_guard].index(max(data[selected_guard]))

		print(int(selected_guard) * int(selected_time))
	except Exception as e:
		raise e


if __name__ == '__main__':
	main()
