def pretty_print(data):
    image = ""
    for line in data:
        image += "\n" + " ".join(line)
    print(image)


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Direction:
    def __init__(self, rotation=0):
        self.rotation: int = rotation

    def rotate(self, dir: int):
        self.rotation += dir
        self.rotation = self.rotation % 4

    @property
    def x(self):
        if self.rotation == 1:
            return 1
        elif self.rotation == 3:
            return -1
        else:
            return 0

    @property
    def y(self):
        if self.rotation == 0:
            return -1
        elif self.rotation == 2:
            return 1
        else:
            return 0


class Guard:
    def __init__(self, location: Location, direction: Direction):
        self.location = location
        self.direction = direction

    def update(self, data):
        if self.check_collision(data):
            self.direction.rotate(1)
        if not self.check_collision(data):
            self.location.x += self.direction.x
            self.location.y += self.direction.y

    def check_collision(self, data):
        next_space = Location(
            self.location.x + self.direction.x, self.location.y + self.direction.y
        )
        if in_bounds(next_space, len(data[0]), len(data)) and (
            data[next_space.y][next_space.x] == "#"
            or data[next_space.y][next_space.x] == "O"
        ):
            return True
        else:
            return False


def in_bounds(pos: Location, x, y):
    if pos.x >= 0 and pos.x < x and pos.y >= 0 and pos.y < y:
        return True
    return False


def draw_map(file: list[list], pos: Location, prev_spot: Location):
    draw = [line.copy() for line in file]
    draw[prev_spot.y][prev_spot.x] = "\x1b[6;30;93m" + "^" + "\x1b[0m"
    draw[pos.y][pos.x] = "\x1b[6;30;42m" + "^" + "\x1b[0m"
    # print("")
    pretty_print(draw)
    # print("\033[4A\033[2K", end="")


def draw_local_map(file, pos):
    draw = [line.copy() for line in file]

    x_low = max(pos.x - 10, 0)
    x_high = min(len(file[0]), pos.x + 10)
    y_low = max(pos.y - 10, 0)
    y_high = min(len(file[0]), pos.y + 10)

    draw[pos.y][pos.x] = "\x1b[6;30;42m" + "^" + "\x1b[0m"
    # print("")
    draw = draw[y_low:y_high]
    draw = [line[x_low:x_high] for line in draw]
    pretty_print(draw)


def part1():
    with open("data.txt", "r") as f:
        file = f.readlines()

    file = list(map(str.strip, file))
    file = [[*s] for s in file]

    # Find guard position
    guard_loc = []

    for y in range(len(file)):
        for x in range(len(file[0])):
            if file[y][x] == "^":
                guard_loc = Location(x, y)
                file[y][x] = "."
                break
        if guard_loc:
            break

    guard = Guard(guard_loc, Direction())

    x_bound = len(file[0])
    y_bound = len(file)

    spaces = []

    while in_bounds(guard.location, x_bound, y_bound):
        # draw_map(file, guard.location, prev_spot)
        prev_spot = (guard.location.x, guard.location.y)
        spaces.append(prev_spot)
        guard.update(file)

        # time.sleep(0.2)

    draw = [line.copy() for line in file]

    for pos in spaces:
        draw[pos[1]][pos[0]] = "X"

    # pretty_print(draw)

    unique_spaces = set(spaces)
    print(len(unique_spaces))


# Bruteforce time
def part2():
    with open("data.txt", "r") as f:
        file = f.readlines()

    file = list(map(str.strip, file))
    file = [[*s] for s in file]

    # Find guard position
    guard_loc_x = 0
    guard_loc_y = 0

    for y in range(len(file)):
        stop = False
        for x in range(len(file[0])):
            if file[y][x] == "^":
                stop = True
                guard_loc_x = x
                guard_loc_y = y
                file[y][x] = "."
                break
        if stop:
            break

    guard_loc = Location(guard_loc_x, guard_loc_y)
    guard = Guard(guard_loc, Direction())

    x_bound = len(file[0])
    y_bound = len(file)

    spaces = []

    while in_bounds(guard.location, x_bound, y_bound):
        # draw_map(file, guard.location, prev_spot)
        prev_spot = (guard.location.x, guard.location.y)
        spaces.append(prev_spot)
        guard.update(file)

        # time.sleep(0.2)

    spaces = list(set(spaces[1:]))  # Don't include the start spot
    loops = []
    for obstacle in spaces:
        guard_loc = Location(guard_loc_x, guard_loc_y)
        guard = Guard(guard_loc, Direction())

        file[obstacle[1]][obstacle[0]] = "O"

        potential_loop_pos = []
        while in_bounds(guard.location, x_bound, y_bound):
            # Loops only really happen on a turn
            if guard.check_collision(file):
                # If a turn has already been visited in the same direction then it's a loop
                if (
                    guard.location.x,
                    guard.location.y,
                    guard.direction.rotation,
                ) in potential_loop_pos:
                    # draw_local_map(test_loop_map, bruteforce_guard.location)
                    loops.append(obstacle)
                    break

                # If it hasnt been visited add it to the list of turns to check
                potential_loop_pos.append(
                    (
                        guard.location.x,
                        guard.location.y,
                        guard.direction.rotation,
                    )
                )
            _ = guard.update(file)
        file[obstacle[1]][obstacle[0]] = "."

    loops = list(set(loops))

    print("Result:")
    print(len(loops))


import time

if __name__ == "__main__":
    part1()
    start = time.perf_counter()
    part2()
    stop = time.perf_counter()
    print(stop - start, "seconds")
