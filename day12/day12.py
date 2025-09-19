def read_data():
    with open("data.txt") as f:
        file = f.readlines()
        file = [str.strip(line) for line in file]

    # A 2D list seems appropriate for now
    data = [list(line) for line in file]
    return data


def debug_print_field(data):
    for line in data:
        print(" ".join(line))


def floodfill_plots(data, x, y):
    mod = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    plots = []
    to_be_checked = [(x, y)]
    letter = data[y][x]

    while to_be_checked:
        cur_x, cur_y = to_be_checked.pop()

        plots.append((cur_x, cur_y))
        for mx, my in mod:
            lx = cur_x + mx
            ly = cur_y + my

            x_is_valid = lx >= 0 and lx < len(data[0])
            y_is_valid = ly >= 0 and ly < len(data)

            # Guard for out of bounds
            if not x_is_valid or not y_is_valid:
                continue

            # Guard against self reshecking
            if (lx, ly) in plots or (lx, ly) in to_be_checked:
                continue

            if data[ly][lx] == letter:
                to_be_checked.append((lx, ly))
    return plots


def is_in_plots(x, y, all_plots):
    for p in all_plots:
        if (x, y) in p:
            return True

    return False


def part1(data: list[list[str]]):
    # debug_print_field(data)

    groups = []

    # Create the plots
    print("  Generating islands")
    for y, line in enumerate(data):
        for x, _ in enumerate(line):
            if is_in_plots(x, y, groups):
                continue
            groups.append(floodfill_plots(data, x, y))

    # Area is now the len() of a group

    # Time to figure out the perimiter
    print("  Calculating perimiters")
    cost = 0
    for group in groups:
        perimiter = 0
        for plot in group:
            x, y = plot

            mods = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            plot_perimiter = 4

            for mX, mY in mods:
                if (x + mX, y + mY) in group:
                    plot_perimiter -= 1

            perimiter += plot_perimiter

        cost += len(group) * perimiter

    print("    Final cost:", cost)


def part2(data: list[list[str]]):
    # debug_print_field(data)

    groups = []

    # Create the plots
    print("  Generating islands")
    for y, line in enumerate(data):
        for x, _ in enumerate(line):
            if is_in_plots(x, y, groups):
                continue
            groups.append(floodfill_plots(data, x, y))

    # Area is now the len() of a group

    # Time to figure out the sides
    print("  Calculating sides")
    cost = 0
    iters = 0
    for group in groups:
        # N-Sides == N-Corners so lets find all the corners
        corners = 0
        for plot in group:
            side_mods = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
            corner_pairs = list(zip(side_mods, side_mods[1:]))
            x, y = plot

            for direction in corner_pairs:
                legs = 0
                for mX, mY in direction:
                    if (x + mX, y + mY) not in group:
                        legs += 1

                if legs == 2:
                    corners += 1

                elif legs == 0:
                    corner_mod = [0, 0]
                    for mX, mY in direction:
                        corner_mod[0] += mX
                        corner_mod[1] += mY

                    if (x + corner_mod[0], y + corner_mod[1]) not in group:
                        corners += 1

        cost += corners * len(group)
        iters += 1
    print("    Final cost:", cost)


if __name__ == "__main__":
    print("Part 1")
    part1(read_data())
    print("\nPart 2")
    part2(read_data())
