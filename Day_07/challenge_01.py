#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 7, challenge 1
https://adventofcode.com/2018/day/7

- Read the input file which contains instructions for a product assembly.
- The instructions specify a series of steps and requirements about which steps must be finished before others can begin.
- Determine the order in which the steps should be completed.
    If more than one step is ready, choose the step which is first alphabetically.
"""

import os
import re

INPUT_FILENAME = 'input.txt'


class Step:
    def __init__(self, name):
        self.parent = []
        self.children = []
        self.name = name

    def is_ready(self):
        return len(self.parent) == 0

    def __lt__(self, other):
        return self.name < other.name


def link(parent_step, child_step):
    parent_step.children.append(child_step)
    child_step.parent.append(parent_step)


def init(input):
    line_structure = 'Step [A-Z]{1} must be finished before step [A-Z]{1} can begin.'
    steps = {}
    for index, line in enumerate(input):
        matcher = re.fullmatch(line_structure, line.strip())
        if matcher is None:
            print('Failed to match pattern on line #{}'.format(index))
            raise ValueError('String on line {} is not in the expected format.'.format(index))
        words = line.split()
        parent = words[1]
        child = words[7]
        if parent not in steps:
            steps[parent] = Step(parent)
        if child not in steps:
            steps[child] = Step(child)
        link(steps[parent], steps[child])
    return steps


def insert_sorted_letter(steps_list, step):
    i = 0
    while i < len(steps_list) and steps_list[i] < step:
        i += 1
    steps_list.insert(i, step)


def main():
    try:
        with open(__file__.replace(os.path.basename(__file__), INPUT_FILENAME)) as f:
            steps = init(f.readlines())
        available = []
        done = []

        for step in list(steps.values()):
            if step.is_ready():
                insert_sorted_letter(available, step)

        while len(available) > 0:
            next_step = available.pop(0)
            done.append(next_step.name)
            for child in next_step.children:
                child.parent.remove(next_step)
                if child.is_ready():
                    insert_sorted_letter(available, child)

        print(''.join(done))

    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
