#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import react_polymer, remove_triggered_pairs


def solve(input_text):
    return len(react_polymer(input_text))


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
