#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest

from shared.utils import get_input
from . import solution1, solution2, common


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


class TestCommon(unittest.TestCase):
    module = common
    test_input = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]
    test_coords = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]

    def test_parse(self):
        self.assertEqual(self.test_coords, self.module.parse(self.test_input))

    def test_get_max_x_and_y(self):
        x, y = self.module.get_max_x_and_y(self.test_coords)
        self.assertEqual(8, x)
        self.assertEqual(9, y)

    def test_create_empty_grid(self):
        grid = self.module.create_empty_grid(self.test_coords)
        self.assertEqual(9, len(grid))  # horizontal
        self.assertEqual(10, len(grid[0]))  # vertical
        for col in grid:
            for cell in col:
                self.assertIsNone(cell)


class TestSolution1(TestSolution):
    module = solution1
    expected = "lorem ipsum!"

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