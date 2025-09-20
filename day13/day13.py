from dataclasses import dataclass
import math


@dataclass
class Button:
    x: int
    y: int


@dataclass
class Prize:
    x: int
    y: int


# (Yes these have the same interface but it feels nice and semantically they mean different things)


@dataclass
class Machine:
    a: Button
    b: Button
    prize: Prize


# Assumes the data ends with a empty line
def read_data():
    with open("data.txt") as f:
        file = f.read()
    data = file.split("\n")
    data = [str.strip(line) for line in data]

    machines = []
    machine_buffer = []
    for line in data:
        if "Button" in line:
            coords = line[10:].split(", ")
            machine_buffer.append(Button(int(coords[0][2:]), int(coords[1][2:])))

        if "Prize" in line:
            coords = line[7:].split(", ")
            machine_buffer.append(Prize(int(coords[0][2:]), int(coords[1][2:])))

        if line == "":
            machines.append(
                Machine(machine_buffer[0], machine_buffer[1], machine_buffer[2])
            )
            machine_buffer = []

    return machines


def inverse(a: Button, b: Button):
    norm = 1 / (a.x * b.y - a.y * b.x)

    return [[b.y * norm, -b.x * norm], [-a.y * norm, a.x * norm]]


def matrix_mult(a: Button, b: Button, prize: Prize, add):
    inv = inverse(a, b)

    px = prize.x + add
    py = prize.y + add
    x = inv[0][0] * px + inv[0][1] * py
    y = inv[1][0] * px + inv[1][1] * py

    return x, y


round_err = 0.001


# This is just a linear algebra problem, so we just use the inverse matrix
def solution(data: list[Machine], add=0):
    if add == 0:
        MAX_PRESSES = 100
    else:
        MAX_PRESSES = math.inf

    tokens = 0
    for m in data:
        x, y = matrix_mult(m.a, m.b, m.prize, add)

        if (
            abs(x - round(x))
            < round_err  # Learning moment: math.isclose is not better than this
            and abs(y - round(y)) < round_err
            and x <= MAX_PRESSES
            and y <= MAX_PRESSES
            and x > 0
            and y > 0
        ):
            tokens += round(x) * 3
            tokens += round(y)
    return tokens


if __name__ == "__main__":
    data = read_data()
    print("Part 1: ", solution(data))
    print("Part 2: ", solution(data, 10000000000000))
