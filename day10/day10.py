def part1():
    with open("data.txt", "r") as f:
        file = f.readlines()
    file = list(map(str.strip, file))

    topo = [[int(x) for x in line] for line in file]

    starts = []

    for y, line in enumerate(topo):
        for x, point in enumerate(line):
            if point == 0:
                starts.append((x, y))

    score = 0

    for start in starts:
        s = set()

        recursive_traverse(start, topo, s)

        score += len(s)

    print(score)


def recursive_traverse(point, topo, met):
    x = point[0]
    y = point[1]

    current = topo[y][x]

    if current == 9:
        met.add((x, y))
        return

    # print(x, y)
    if x - 1 >= 0 and topo[y][x - 1] == current + 1:
        recursive_traverse((x - 1, y), topo, met)

    if y - 1 >= 0 and topo[y - 1][x] == current + 1:
        recursive_traverse((x, y - 1), topo, met)

    if y + 1 < len(topo) and topo[y + 1][x] == current + 1:
        recursive_traverse((x, y + 1), topo, met)

    if x + 1 < len(topo) and topo[y][x + 1] == current + 1:
        recursive_traverse((x + 1, y), topo, met)


def part2():
    with open("data.txt", "r") as f:
        file = f.readlines()
    file = list(map(str.strip, file))

    topo = [[int(x) for x in line] for line in file]

    starts = []

    for y, line in enumerate(topo):
        for x, point in enumerate(line):
            if point == 0:
                starts.append((x, y))

    score = 0

    for start in starts:

        score += recursive_traverse_2(start, topo)

    print(score)


def recursive_traverse_2(point, topo):
    x = point[0]
    y = point[1]

    current = topo[y][x]

    if current == 9:
        return 1

    score = 0

    if x - 1 >= 0 and topo[y][x - 1] == current + 1:
        score += recursive_traverse_2((x - 1, y), topo)

    if y - 1 >= 0 and topo[y - 1][x] == current + 1:
        score += recursive_traverse_2((x, y - 1), topo)

    if y + 1 < len(topo) and topo[y + 1][x] == current + 1:
        score += recursive_traverse_2((x, y + 1), topo)

    if x + 1 < len(topo) and topo[y][x + 1] == current + 1:
        score += recursive_traverse_2((x + 1, y), topo)
    return score


if __name__ == "__main__":
    part1()
    part2()
