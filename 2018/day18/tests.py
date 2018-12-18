#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2
from .lumber import LumberCollectionArea


SOLUTION_DIR = Path(__file__).parent


class TestSolution(unittest.TestCase):
    module = None
    input_filename = "test_input.txt"
    expected = None

    def setUp(self):
        if self.module is None:
            raise NotImplementedError(
                "subclasses of TestSolution must provide module to test"
            )
        if self.expected is None:
            raise NotImplementedError(
                "subclasses of TestSolution must provide expected value"
            )
        self.input_path = SOLUTION_DIR.joinpath(self.input_filename)
        self.input_text = get_input(self.input_path)


class ValuesToTest:
    test_input = [
        ".#.#...|#.",
        ".....#|##|",
        ".|..|...#.",
        "..|#.....#",
        "#.#|||#|#|",
        "...#.||...",
        ".|....|...",
        "||...#|.#|",
        "|.||||..|.",
        "...#.|..|.",
    ]
    initial_str = (
        ".#.#...|#.\n"
        ".....#|##|\n"
        ".|..|...#.\n"
        "..|#.....#\n"
        "#.#|||#|#|\n"
        "...#.||...\n"
        ".|....|...\n"
        "||...#|.#|\n"
        "|.||||..|.\n"
        "...#.|..|."
    )


class TestLumberCollectionArea(unittest.TestCase, ValuesToTest):
    def test_constructor(self):
        area = LumberCollectionArea(self.test_input)
        self.assertEqual(self.initial_str, str(area))

    def test_get(self):
        values_to_test = [
            (0, 0, "."),
            (0, 4, "#"),
            (0, 9, "."),
            (4, 0, "."),
            (9, 0, "."),
            (9, 4, "|"),
            (9, 9, "."),
            (4, 9, "."),
            (4, 4, "|")
        ]
        area = LumberCollectionArea(self.test_input)

        for x, y, expected in values_to_test:
            self.assertEqual(expected, area.get(x, y))

    def test_get_surrounding_square_contents(self):
        values_to_test = [
            (0, 0, 0, 1, 2),
            (0, 9, 1, 0, 2),
            (9, 0, 1, 2, 0),
            (9, 9, 2, 0, 1),
            (5, 5, 4, 1, 3),
        ]
        area = LumberCollectionArea(self.test_input)

        for x, y, num_trees, num_lumberyards, num_open in values_to_test:
            surrounding = area.get_surrounding_square_contents(x, y)

            self.assertEqual(num_trees, surrounding["|"])
            self.assertEqual(num_lumberyards, surrounding["#"])
            self.assertEqual(num_open, surrounding["."])


class TestSolution1(TestSolution):
    module = solution1
    expected = 1147

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = "lorem ipsum?"

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
