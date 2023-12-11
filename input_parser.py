
import os
import sys


def input_parser(day):
    with open(f'./inputs/{day}.txt', 'r') as f:
        return [line.strip('\n') for line in f]
            