#! /usr/bin/env python3

"""
Advent Of Code 2018, Day 7, challenge 2
https://adventofcode.com/2018/day/7

- Read the input file which contains instructions for a product assembly.
- The instructions specify a series of steps and requirements about which steps must be finished before others can begin.
- With 5 workers, each working on a single step - how long will it take to complete the product's assembly?
"""

import os
import re

INPUT_FILENAME = 'input.txt'
MAX_WORKERS = 5


class Step:
    def __init__(self, name):
        self.parent = []
        self.children = []
        self.name = name
        self.completion_time = 60 + (ord(self.name) - ord('A') + 1)

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
        elapsed_time = 0
        workers = []

        for step in list(steps.values()):
            if step.is_ready():
                insert_sorted_letter(available, step)

        # Assign jobs to workers
        while available and len(workers) < MAX_WORKERS:
            workers.append(available.pop(0))

        while available or workers:
            i = 0
            while i < len(workers):
                work = workers[i]
                work.completion_time -= 1
                if work.completion_time == 0:
                    workers.remove(work)
                    for child in work.children:
                        child.parent.remove(work)
                        if child.is_ready():
                            insert_sorted_letter(available, child)
                else:
                    i += 1
            # Assign jobs to idle workers
            while available and len(workers) < MAX_WORKERS:
                workers.append(available.pop(0))
            elapsed_time += 1

        print(str(elapsed_time))

    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
