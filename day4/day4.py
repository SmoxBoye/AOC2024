def check_spot(x, y, data):

    directions = []

    for dir in [1, -1]:

        if x + dir * 3 >= 0 and x + dir * 3 < len(data[x]):
            directions.append(
                "".join([data[y][x + i * dir] for i in range(4)])
            )  # Right/Left

        if y + dir * 3 >= 0 and y + dir * 3 < len(data):
            directions.append(
                "".join([data[y + i * dir][x] for i in range(4)])
            )  # Down/Up

        if (
            y + dir * 3 >= 0
            and y + dir * 3 < len(data)
            and x + dir * 3 >= 0
            and x + dir * 3 < len(data[x])
        ):
            directions.append(
                "".join([data[y + i * dir][x + i * dir] for i in range(4)])
            )  # Southeast/Northwest
        if (
            y + dir * 3 >= 0
            and y + dir * 3 < len(data)
            and x + -dir * 3 >= 0
            and x + -dir * 3 < len(data[x])
        ):
            directions.append(
                "".join([data[y + i * dir][x + i * -dir] for i in range(4)])
            )  # Southwest/Northeast

    hits = 0
    for xmas in directions:
        if xmas == "XMAS":
            hits += 1

    return hits


def part1():
    with open("data.txt", "r") as f:
        file = f.readlines()

    file = list(map(str.strip, file))

    result = 0
    for y in range(len(file)):
        for x in range(len(file[0])):
            if file[y][x] == "X":
                result += check_spot(x, y, file)

    print(result)
    # for line in file:
    #     print(line)


def check_X_spot(x, y, data):

    directions = []

    for dir in [1, -1]:

        directions.append(
            "".join([data[y + i * dir][x + i * dir] for i in range(-1, 2)])
        )  # Southeast/Northwest

        directions.append(
            "".join([data[y + i * dir][x + i * -dir] for i in range(-1, 2)])
        )  # Southwest/Northeast

    hits = 0
    for xmas in directions:
        if (
            xmas == "MAS"
        ):  # Yes i could just check the corners instead of the whole words, no im not going to change the pattern from part1
            hits += 1

    return hits == 2


def part2():
    with open("data.txt", "r") as f:
        file = f.readlines()

    file = list(map(str.strip, file))

    result = 0
    for y in range(1, len(file) - 1):
        for x in range(1, len(file[0]) - 1):
            if file[y][x] == "A":
                if check_X_spot(x, y, file):
                    result += 1

    print(result)
    # for line in file:
    #     print(line)


if __name__ == "__main__":
    part1()
    part2()
