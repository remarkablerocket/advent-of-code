#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse
from .tree import Tree


def sum_nodes(node):
    if not node.children:
        return sum(node.meta)
    else:
        return sum(
            sum_nodes(node.children[n - 1])
            for n in node.meta
            if 0 < n <= len(node.children)
        )


def solve(input_text):
    tree = Tree(parse(input_text))
    return sum_nodes(tree)


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
