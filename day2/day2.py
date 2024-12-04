def safe_range(a, b):
    diff = abs(a - b)
    if diff > 0 and diff < 4:
        return True
    return False


def direction(a, b, up):
    if up:
        if a > b:
            return False
    else:
        if a < b:
            return False

    return True


def part1():
    with open("data.txt", "r") as f:
        file = f.readlines()

    data = []

    # Parse
    for report in file:
        line = report.split(" ")
        rep = [int(x) for x in line]
        data.append(rep)

    # Solve
    safe_reports = 0

    for report in data:

        up = False
        if report[0] < report[1]:
            up = True

        ok = True
        for level in zip(report, report[1:]):

            if not safe_range(level[0], level[1]):
                ok = False
                break

            if not direction(level[0], level[1], up):
                ok = False
                break

        if ok:
            safe_reports += 1

    print(safe_reports)


def is_safe(a, b, up):
    if safe_range(a, b) and direction(a, b, up):
        return True
    return False


def validate(report):
    up = False
    if report[0] < report[1]:
        up = True

    ok = True

    for level in zip(report, report[1:]):
        if not is_safe(level[0], level[1], up):
            ok = False

            break
    return ok


def part2():
    with open("data.txt", "r") as f:
        file = f.readlines()

    data: list[list[int]] = []

    # Parse
    for report in file:
        line = report.split(" ")
        rep = [int(x) for x in line]
        data.append(rep)

    # Solve
    safe_reports = 0
    for report in data:
        ok = validate(report)

        if not ok:
            for i in range(
                len(report)
            ):  # I hate bruteforcing this, not epic, didn't laugh
                ok = validate(report[:i] + report[i + 1 :])
                if ok:
                    break

        if ok:
            # print(report)
            safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    part1()
    part2()
