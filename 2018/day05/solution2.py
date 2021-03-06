#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import react_polymer, remove_triggered_pairs


def get_unit_types(text):
    unit_types = set(char.upper() for char in text)

    return "".join(unit_types)


def remove_unit_type(unit_type, text):
    text = text.replace(unit_type, "")
    text = text.replace(unit_type.lower(), "")
    return text


def solve(input_text):
    shortest_length = 99999  # longer than solution to part 1

    for unit_type in get_unit_types(input_text):
        new_text = remove_unit_type(unit_type, input_text)
        length = len(react_polymer(new_text))
        if length < shortest_length:
            shortest_length = length

    return shortest_length


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)[0]
    solution = solve(input_text)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
