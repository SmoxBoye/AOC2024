import itertools as it


def part1():
    with open("data.txt", "r") as f:
        file = f.readlines()
    file = list(map(str.strip, file))

    data = [line.split(": ") for line in file]

    for i, line in enumerate(data):
        data[i][1] = list(map(int, data[i][1].split(" ")))
        data[i][0] = int(data[i][0])

    answer = 0

    for eq in data:
        operators = [x for x in it.product(["+", "*"], repeat=len(eq[1]) - 1)]
        for combination in operators:
            res = eq[1][0]
            for i, op in enumerate(combination):
                if op == "+":
                    res += eq[1][i + 1]
                if (
                    op == "*"
                ):  # I could put an else here but i suspect that more is going to get added in part 2
                    res *= eq[1][i + 1]
            if res == eq[0]:
                answer += res
                break

    print(answer)


def part2():
    with open("data.txt", "r") as f:
        file = f.readlines()
    file = list(map(str.strip, file))

    data = [line.split(": ") for line in file]

    for i, line in enumerate(data):
        data[i][1] = list(map(int, data[i][1].split(" ")))
        data[i][0] = int(data[i][0])

    answer = 0

    for eq in data:
        operators = [x for x in it.product(["+", "*", "||"], repeat=len(eq[1]) - 1)]
        for combination in operators:
            res = eq[1][0]
            for i, op in enumerate(combination):
                if op == "+":
                    res += eq[1][i + 1]
                if op == "*":
                    res *= eq[1][i + 1]
                if op == "||":  # I was right
                    res = int(str(res) + str(eq[1][i + 1]))
            if res == eq[0]:
                answer += res
                break

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
