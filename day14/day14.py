from dataclasses import dataclass
import math
# Initial thoughts:
# We should be able to calculate where the robot will end up in a single math equation with some modulo


@dataclass
class Velocity:
    x: int
    y: int


@dataclass
class Robot:
    x: int
    y: int
    v: Velocity


def read_data(filename: str) -> list[Robot]:
    with open(filename) as f:
        file = f.readlines()

    data = [line.strip() for line in file]
    data = [line.split(" ") for line in data]

    robots = []

    for r in data:
        pos = r[0][2:].split(",")
        vel = r[1][2:].split(",")

        robots.append(
            Robot(int(pos[0]), int(pos[1]), Velocity(int(vel[0]), int(vel[1])))
        )
    return robots


def safety_factor(robots: list[Robot], size_x, size_y):
    middle_x = size_x // 2
    middle_y = size_y // 2

    ul = 0
    ur = 0
    dl = 0
    dr = 0

    for robot in robots:
        up = robot.y > middle_y
        down = robot.y < middle_y
        right = robot.x > middle_x
        left = robot.x < middle_x

        if up and right:
            ur += 1
        elif up and left:
            ul += 1
        elif down and right:
            dr += 1
        elif down and left:
            dl += 1

    return ul * ur * dl * dr


# Im gonna hard-predict that we need to simulate some ridiculous number of timesteps later.
# If im gonna need to do robots bouncing off each other im gonna be screwed lmao
def part1(data: list[Robot], timesteps: int, size: tuple, tree=False):
    map_x = size[0]
    map_y = size[1]

    for robot in data:
        robot.x = (robot.x + robot.v.x * timesteps) % map_x
        robot.y = (robot.y + robot.v.y * timesteps) % map_y

    safety = safety_factor(data, map_x, map_y)
    if not tree:
        print(safety)
    return data, safety


def print_robots(data: list[Robot], size: tuple):
    map = [[0 for _ in range(size[0])] for _ in range(size[1])]

    for robot in data:
        map[robot.y][robot.x] += 1

    for line in map:
        print("".join([str(x) for x in line]).replace("0", "."))

    print("\n" * 4)


# We can use safety_factor as entropy and use that as a metric (hint from reddit)
def part2(data: list[Robot], size: tuple):
    MAX = 10_000

    lowest_safety = math.inf
    for i in range(MAX):
        data, safety = part1(data, 1, size, True)
        if safety < lowest_safety:
            print("PRINTING: ", i + 1)
            print_robots(data, size)
            lowest_safety = safety


if __name__ == "__main__":
    filename = "data.txt"
    example_map = (11, 7)
    bathroom_map = (101, 103)
    print("Part 1")
    part1(read_data(filename), 100, bathroom_map)
    print("Press a button to go to part 2 (will effectively flush the screen)")
    hold = input()
    part2(read_data(filename), bathroom_map)
