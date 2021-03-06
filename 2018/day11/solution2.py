#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .common import get_cell_power_level


def get_squares_power(x, y, grid, size=3):
    to_deduct = 0

    if x > 0:
        to_deduct += grid[x - 1][y + size - 1]
    if y > 0:
        to_deduct += grid[x + size - 1][y - 1]
    if x > 0 and y > 0:
        to_deduct -= grid[x - 1][y - 1]

    return grid[x + size - 1][y + size - 1] - to_deduct


def get_best_square(grid):
    best_power = 0
    best_x = None
    best_y = None
    best_size = None

    for size in range(1, 301):
        for x in range(300):
            if (size + x) > 300:
                break
            for y in range(300):
                if (size + y) > 300:
                    break
                power = get_squares_power(x, y, grid, size)
                if power > best_power:
                    best_power = power
                    best_x = x
                    best_y = y
                    best_size = size

        # Uncomment the following line to get runtime down to ~1 sec
        # if size > (best_size + 5): break

    return (best_x + 1, best_y + 1, best_size)


def create_optimised_grid(input_value):
    grid = []

    for x in range(300):
        grid.append([])

        for y in range(300):
            grid[x].append(get_cell_power_level(x + 1, y + 1, input_value))

            if y > 0:
                grid[x][y] += grid[x][y - 1]  # add value from cell above
            if x > 0:
                grid[x][y] += grid[x - 1][y]  # add value from cell to the left
            if x > 0 and y > 0:
                grid[x][y] -= grid[x - 1][y - 1]  # remove double counted region

    return grid


def solve(input_value):
    grid = create_optimised_grid(input_value)
    x, y, size = get_best_square(grid)

    return "{},{},{}".format(x, y, size)


if __name__ == '__main__':
    from timeit import default_timer as timer

    start = timer()

    input_value = 9798
    solution = solve(input_value)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
