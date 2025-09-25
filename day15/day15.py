from enum import Enum


class Dir(Enum):
    up = 0
    right = 1
    down = 2
    left = 3


class Node(Enum):
    wall = 0
    air = 1
    box = 2
    robot = 3


def read_data(filename: str):
    with open(filename) as f:
        file = f.readlines()

    file = [line.strip() for line in file]

    map = []

    instructions = []

    done_with_map = False
    for line in file:
        if line == "":
            done_with_map = True
            continue

        if not done_with_map:  # Doing it in the order of the data
            map.append(line)
        else:
            instructions.append(line)

    parsed_map = []
    player_pos = None
    for y, line in enumerate(map):
        parsed_line = []
        for x, cell in enumerate(line):
            match cell:
                case "#":
                    parsed_line.append(Node.wall)
                case ".":
                    parsed_line.append(Node.air)
                case "O":
                    parsed_line.append(Node.box)
                case "@":
                    parsed_line.append(Node.robot)
                    player_pos = (x, y)
        parsed_map.append(parsed_line)

    assert player_pos, "Player not found"

    instructions = "".join(instructions)

    parsed_instructions = []

    for instr in instructions:
        match instr:
            case "^":
                parsed_instructions.append(Dir.up)
            case ">":
                parsed_instructions.append(Dir.right)
            case "v":
                parsed_instructions.append(Dir.down)
            case "<":
                parsed_instructions.append(Dir.left)

    return parsed_map, parsed_instructions, player_pos


def part1(map, instructions, player_pos):
    pass


if __name__ == "__main__":
    filename = "example.txt"
    part1(*read_data(filename))
