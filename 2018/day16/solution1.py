#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

def addr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] + reg[b]
    return reg


def addi(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] + b
    return reg

def mulr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] * reg[b]
    return reg


def muli(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] * b
    return reg


def banr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] & reg[b]
    return reg


def bani(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] & b
    return reg


def borr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] | reg[b]
    return reg


def bori(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] | b
    return reg


def setr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a]
    return reg


def seti(a, b, c, reg):
    reg = reg[:]
    reg[c] = a
    return reg


def gtir(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(a > reg[b])
    return reg


def gtri(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] > b)
    return reg


def gtrr(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] > reg[b])
    return reg


def eqir(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(a == reg[b])
    return reg


def eqri(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] == b)
    return reg


def eqrr(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] == reg[b])
    return reg




def parse(input_text):
    instructions = []
    current_instruction = []
    last_line = None

    for line in input_text:
        if not line:
            if not last_line:
                break
            else:
                instructions.append(current_instruction)
                current_instruction = []

        elif line.split()[0] in ["Before:", "After:"]:
            current_instruction.append([
                int(c) for c in line[9: -1].split(", ")
            ])
        else:
            current_instruction.append([int(c) for c in line.split()])

        last_line = line

    return instructions


def solve(input_text):
    opcodes = [
        addr, addi, mulr, muli, banr, bani, borr, bori,
        setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
    ]
    instructions = parse(input_text)

    answer = 0

    for before, (op, a, b, c), after in instructions:
        count = 0
        for opcode in opcodes:
            try:
                reg = opcode(a, b, c, before)
            except IndexError:
                pass
            else:
                if reg == after:
                    count += 1

        if count >= 3:
            answer += 1

    return answer


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
