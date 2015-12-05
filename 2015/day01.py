#!/usr/bin/env python
"""
Solution for Advent of Code day 1
http://adventofcode.com/day/1
"""
from __future__ import print_function
from collections import Counter

# Part 1
def find_end_floor(directions):
    counter = Counter(directions)
    floor = counter['('] - counter[')']
    return floor

# Part 2
def find_first_step_underground(directions):
    floor = 0
    for step in enumerate(directions, 1):
        if step[1] == '(':
            floor += 1
        elif step[1] == ')':
            floor -= 1
        if floor < 0:
            return step[0]

def load_input():
    with open('data/day01_input.txt') as input_file:
        directions = input_file.read()
        return directions

if __name__ == '__main__':
    directions = load_input()
    floor = find_end_floor(directions)
    print('Ending floor: {0}'.format(floor))
    underground_step = find_first_step_underground(directions)
    print('First underground step: {0}'.format(underground_step))
