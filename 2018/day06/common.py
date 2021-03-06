#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(input_text):
    return [(int(x), int(y)) for x, y in (line.split(", ") for line in input_text)]


def get_max_x_and_y(coords):
    x = max(coord[0] for coord in coords)
    y = max(coord[1] for coord in coords)
    return x, y


def get_manhattan_distance(x, y, coord):
    return abs(x - coord[0]) + abs(y - coord[1])


def complete_grid(coords, func):
    max_x, max_y = get_max_x_and_y(coords)
    x_range = range(max_x + round(max_x / 10) + 1)
    y_range = range(max_y + round(max_y / 10) + 1)

    grid = [
        [
            func(x, y, coords) for x in x_range
        ] for y in y_range
    ]

    return grid
