#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 5, challenge 2
https://adventofcode.com/2018/day/5

- Read the input file which contains the description of a polymer using 50,000 characters
	The polymer is formed by units, which represented by a single character.
	Units' polarity is represented by capitalization.
		For example - 'A' and 'a' represents the same unit with opposite polarity.
	When reacting the polymer - any two adjacent units of the same type and reversed polarity are destroyed.
- Remove all instances of a selected unit (both polarities) and check the length of the new reacted polymer.
- Return the length of the shortest polymer possible when removing only one unit from it.
"""

import os

INPUT_FILENAME = 'input.txt'


def main():
    try:
        file = os.path.join(os.getcwd(), INPUT_FILENAME)
        with open(file) as f:
            polymer = list(f.read().strip())

        polymer = react_polymer(polymer)
        units_in_polymer = list({unit.lower() for unit in polymer})

        minimal_length = len(polymer)
        for unit in units_in_polymer:
            new_polymer = list(filter(lambda a: a.lower() != unit, polymer))
            new_polymer_len = len(react_polymer(new_polymer))
            if new_polymer_len < minimal_length:
                minimal_length = new_polymer_len

        print(minimal_length)

    except Exception as e:
        raise e


def react_polymer(polymer):
    i = 1
    while i < len(polymer):
        if polymer[i] == polymer[i - 1].swapcase():
            del polymer[i]
            del polymer[i - 1]
            i = i - 2 if i > 2 else 0
        i += 1
    return polymer


if __name__ == '__main__':
    main()
