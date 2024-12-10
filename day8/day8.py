from collections import defaultdict
from itertools import permutations


def determine_antinode(a, b):
    x_delta = a[0] - b[0]
    y_delta = a[1] - b[1]

    return (a[0] + x_delta, a[1] + y_delta)


def in_bounds(node, x_bound, y_bound):
    if node[0] >= 0 and node[1] >= 0 and node[0] < x_bound and node[1] < x_bound:
        return True
    return False


def part1():
    with open("data.txt", "r") as f:
        file = f.readlines()

    file = list(map(str.strip, file))
    file = [[*s] for s in file]

    X_BOUND = len(file[0])
    Y_BOUND = len(file)

    # Get all the antennas:

    antennas = defaultdict(list)

    for i, y in enumerate(file):
        for j, x in enumerate(y):
            if x != ".":
                antennas[x].append((j, i))

    antinodes = set()

    # Determine antinodes
    for frequency in antennas.keys():
        ant = antennas[frequency]

        if len(ant) > 1:
            for i in range(len(ant)):
                for j in range(i + 1, len(ant)):

                    antinode_a = determine_antinode(ant[i], ant[j])
                    antinode_b = determine_antinode(ant[j], ant[i])

                    if in_bounds(antinode_a, X_BOUND, Y_BOUND):
                        antinodes.add(antinode_a)
                    if in_bounds(antinode_b, X_BOUND, Y_BOUND):
                        antinodes.add(antinode_b)

    print(len(antinodes))


def part2():
    with open("data.txt", "r") as f:
        file = f.readlines()

    file = list(map(str.strip, file))
    file = [[*s] for s in file]

    X_BOUND = len(file[0])
    Y_BOUND = len(file)

    # Get all the antennas:

    antennas = defaultdict(list)

    for i, y in enumerate(file):
        for j, x in enumerate(y):
            if x != ".":
                antennas[x].append((j, i))

    antinodes = set()

    # Determine antinodes
    for frequency in antennas.keys():
        ant = antennas[frequency]

        if len(ant) > 1:
            for i in range(len(ant)):
                for j in range(i + 1, len(ant)):

                    antinode_a = determine_antinode(ant[i], ant[j])

                    prev = ant[i]
                    while in_bounds(antinode_a, X_BOUND, Y_BOUND):
                        antinodes.add(antinode_a)
                        temp_node = antinode_a
                        antinode_a = determine_antinode(antinode_a, prev)
                        prev = temp_node

                    antinode_b = determine_antinode(ant[j], ant[i])
                    prev = ant[j]
                    while in_bounds(antinode_b, X_BOUND, Y_BOUND):
                        antinodes.add(antinode_b)
                        temp_node = antinode_b
                        antinode_b = determine_antinode(antinode_b, prev)
                        prev = temp_node

                    antinodes.add(ant[i])
                    antinodes.add(ant[j])

    # print(antinodes)

    # for node in antinodes:
    #     file[node[1]][node[0]] = "#"

    # for line in file:
    #     print(" ".join(line))

    print(len(antinodes))


if __name__ == "__main__":
    part1()
    part2()
