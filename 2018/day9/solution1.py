#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from .common import parse


def n_places_clockwise(circle, current_marble, n):
    current_marble += n
    current_marble %= len(circle)
    return current_marble


def n_places_counter_clockwise(circle, current_marble, n):
    current_marble -= n
    current_marble %= len(circle)
    return current_marble


def place_marble(circle, current_marble_pos, next_marble):
    current_marble_pos = n_places_clockwise(
        circle, current_marble_pos, 1) + 1
    if current_marble_pos == len(circle):
        circle.append(next_marble)
    else:
        circle.insert(current_marble_pos, next_marble)

    return circle, current_marble_pos


def play_game(num_players, num_marbles):
    players = [0 for n in range(num_players)]

    circle = [0]
    current_marble = 0
    current_player = 0

    for n in range(1, num_marbles + 1):
        if n % 23 == 0:
            points = n
            points += circle[n_places_counter_clockwise(circle, current_marble, 7)]
            players[current_player] += n
            current_marble = n_places_counter_clockwise(
                circle, current_marble, 7)
            players[current_player] += circle.pop(current_marble)
            if current_marble > len(circle):
                curent_marble = 0
        else:
            circle, current_marble = place_marble(circle, current_marble, n)

        current_player += 1
        current_player %= num_players

    return players


def solve(input_text):
    num_players, num_marbles = parse(input_text)
    return max(play_game(num_players, num_marbles))


if __name__ == '__main__':
    from shared.utils import get_input

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)
