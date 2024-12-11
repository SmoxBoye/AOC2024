from functools import cache


@cache  # HAHAHAHAHHAHAHAHAHHA
def recursive_stone_stuff(engraving, depth):

    # Rule 1
    if engraving == 0 and depth > 0:
        engraving = 1
        depth -= 1

    stones = 0

    # Rule 2
    if len(str(engraving)) % 2 == 0 and depth > 0:
        depth -= 1
        engraving = str(engraving)
        half = len(engraving) // 2

        stones += recursive_stone_stuff(int(engraving[:half]), depth)
        stones += recursive_stone_stuff(int(engraving[half:]), depth)
    # Rule 3
    elif depth > 0:
        depth -= 1
        stones += recursive_stone_stuff(engraving * 2024, depth)

    if stones == 0:
        return 1
    else:
        return stones


def part1():
    with open("data.txt", "r") as f:
        file = f.read()

    file = str.split(file, " ")
    file = list(map(int, file))

    stones = 0

    for stone in file:
        stones += recursive_stone_stuff(stone, 25)

    print(stones)


def part2():
    with open("data.txt", "r") as f:
        file = f.read()

    file = str.split(file, " ")
    file = list(map(int, file))

    stones = 0

    for stone in file:
        stones += recursive_stone_stuff(stone, 75)

    print(stones)


if __name__ == "__main__":
    part1()
    part2()
