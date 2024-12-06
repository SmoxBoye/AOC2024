from collections import defaultdict


def check_in(a, b):
    target = min(len(b), len(a))

    count = 0
    for x in a:
        if x in b:
            count += 1

    return count == target


def part1():
    with open("data.txt", "r") as f:
        file = f.readlines()
    file = list(map(str.strip, file))

    # Find split index
    split_index = 0
    for i, line in enumerate(file):
        if line == "":
            split_index = i
            break

    # Split rules and data
    rules, data = file[:split_index], file[split_index + 1 :]

    # Parse rules and data
    rules = [list(map(int, str.split(x, "|"))) for x in rules]
    data = [list(map(int, str.split(x, ","))) for x in data]

    before = defaultdict(set)
    after = defaultdict(set)

    for a, b in rules:
        before[b].add(a)
        after[a].add(b)

    result = 0

    for entry in data:
        ok = True
        for i, item in enumerate(entry):
            check_before = entry[:i]
            check_after = entry[i + 1 :]

            if not len(check_before) == 0 and len(before[item]):
                if not check_in(before[item], check_before):

                    ok = False
                    break
            if not len(check_after) == 0 and len(after[item]):
                if not check_in(after[item], check_after):

                    ok = False
                    break
        if ok:
            result += entry[len(entry) // 2]

    print(result)


def part2():
    with open("data.txt", "r") as f:
        file = f.readlines()
    file = list(map(str.strip, file))

    # Find split index
    split_index = 0
    for i, line in enumerate(file):
        if line == "":
            split_index = i
            break

    # Split rules and data
    rules, data = file[:split_index], file[split_index + 1 :]

    # Parse rules and data
    rules = [list(map(int, str.split(x, "|"))) for x in rules]
    data = [list(map(int, str.split(x, ","))) for x in data]

    before = defaultdict(set)
    after = defaultdict(set)

    for a, b in rules:
        before[b].add(a)
        after[a].add(b)

    to_be_reordered: list[list] = []

    for entry in data:
        ok = True
        for i, item in enumerate(entry):
            check_before = entry[:i]
            check_after = entry[i + 1 :]

            if not len(check_before) == 0 and len(before[item]):
                if not check_in(before[item], check_before):

                    ok = False
                    break
            if not len(check_after) == 0 and len(after[item]):
                if not check_in(after[item], check_after):

                    ok = False
                    break
        if not ok:
            to_be_reordered.append(entry)

    result = 0

    # Ngl im just gonna bubble sort this
    for entry in to_be_reordered:
        for i in range(len(entry)):
            for j in range(i + 1, len(entry)):
                if entry[j] in before[entry[i]]:
                    entry.insert(i, entry.pop(j))

        result += entry[len(entry) // 2]

    print(result)


if __name__ == "__main__":
    part1()
    part2()

# Afterword: Realised AFTER i completed everything that im really only interested in the mid point.
# I realised this after i turned off my brain and sorted on after, entered the result and got it correct, looked back at my code and realised that "that shouldn't have worked, why did it work".
# A super interesting effect of this is that i can flip to sort for both before[entry[i]] and after[entry[i]] on line 121 and (at least on my dataset) the end result is the same.
