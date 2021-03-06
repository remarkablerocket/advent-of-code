#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest
from unittest.mock import patch

from shared.utils import get_input
from . import solution1, solution2


SOLUTION_DIR = Path(__file__).parent


class TestSolution(unittest.TestCase):
    module = None
    input_filename = "test_input.txt"
    expected = None
    claim1_areas = [
        (1, 3), (2, 3), (3, 3), (4, 3),
        (1, 4), (2, 4), (3, 4), (4, 4),
        (1, 5), (2, 5), (3, 5), (4, 5),
        (1, 6), (2, 6), (3, 6), (4, 6),
    ]
    claim2_areas = [
        (3, 1), (4, 1), (5, 1), (6, 1),
        (3, 2), (4, 2), (5, 2), (6, 2),
        (3, 3), (4, 3), (5, 3), (6, 3),
        (3, 4), (4, 4), (5, 4), (6, 4),
    ]
    claim3_areas = [
        (5, 5), (6, 5),
        (5, 6), (6, 6),
    ]

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


class TestSolution1(TestSolution):
    module = solution1
    expected = 4

    def test_parser(self):
        claim1 = solution1.parse_claim(self.input_text[0])
        claim2 = solution1.parse_claim(self.input_text[1])
        claim3 = solution1.parse_claim(self.input_text[2])

        self.assertCountEqual(self.claim1_areas, claim1)
        self.assertCountEqual(self.claim2_areas, claim2)
        self.assertCountEqual(self.claim3_areas, claim3)

    def test_combine_claims(self):
        combined_claims = solution1.combine_claims(
            [self.claim1_areas, self.claim2_areas, self.claim3_areas]
        )
        self.assertEqual(32, len(combined_claims))
        self.assertEqual(1, combined_claims[(4, 1)])
        self.assertEqual(1, combined_claims[(4, 6)])
        self.assertEqual(2, combined_claims[(4, 4)])
        self.assertEqual(0, combined_claims[(4, 8)])

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


class TestSolution2(TestSolution):
    module = solution2
    expected = 3

    def test_parser(self):
        id1, claim1 = solution2.parse_claim(self.input_text[0])
        id2, claim2 = solution2.parse_claim(self.input_text[1])
        id3, claim3 = solution2.parse_claim(self.input_text[2])

        self.assertEqual(1, id1)
        self.assertEqual(2, id2)
        self.assertEqual(3, id3)

        self.assertCountEqual(self.claim1_areas, claim1)
        self.assertCountEqual(self.claim2_areas, claim2)
        self.assertCountEqual(self.claim3_areas, claim3)

    def test_combine_claims(self):
        combined_claims = solution2.combine_claims([
            (1, self.claim1_areas),
            (2, self.claim2_areas),
            (3, self.claim3_areas),
        ])
        self.assertEqual(32, len(combined_claims))
        self.assertEqual(1, combined_claims[(4, 1)])
        self.assertEqual(1, combined_claims[(4, 6)])
        self.assertEqual(2, combined_claims[(4, 4)])
        self.assertEqual(0, combined_claims[(4, 8)])

    def test_check_for_overlaps(self):
        # should probably create this manually rather than rely on
        # combine_claims
        combined_claims = solution2.combine_claims([
            (1, self.claim1_areas),
            (2, self.claim2_areas),
            (3, self.claim3_areas),
        ])
        self.assertTrue(
            solution2.check_for_overlaps(self.claim1_areas, combined_claims)
        )
        self.assertFalse(
            solution2.check_for_overlaps(self.claim3_areas, combined_claims)
        )

    def test_solver(self):
        solution = self.module.solve(self.input_text)
        self.assertEqual(self.expected, solution)


if __name__ == '__main__':
    unittest.main()
