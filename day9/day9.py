def part1():
    with open("data.txt", "r") as f:
        file = f.read()

    # Expand file
    blocks = []

    id = 0

    for i, block in enumerate(file):
        n = int(block)

        if i % 2 == 0:
            tag = id
            id += 1
        else:
            tag = "."

        for i in range(n):
            blocks.append(tag)

    # Compact
    last_space = 0

    for i in range(len(blocks) - 1, 0, -1):
        for j in range(last_space, i):
            if blocks[j] == ".":
                blocks[i], blocks[j] = blocks[j], blocks[i]
                last_space = j
                break

        if last_space >= i:
            break

    answer = 0

    for i, x in enumerate(blocks):
        if type(x) is str:
            break

        answer += i * x

    print(answer)


def part2():
    with open("data.txt", "r") as f:
        file = f.read()

    # Expand file
    blocks = []

    id = 0

    for i, block in enumerate(file):
        n = int(block)

        if i % 2 == 0:
            tag = id
            id += 1
        else:
            tag = "."

        for i in range(n):
            blocks.append(tag)

    # Compact but Defragmented or something

    current = blocks[-1]
    current_len = 0
    left_most_empty = 0

    for i in range(len(blocks) - 1, 0, -1):

        # Nothing found nothing running, move on
        if blocks[i] == "." and current_len == 0:
            continue

        # Block found
        if blocks[i] != "." and current_len == 0:
            current = blocks[i]
        # The block continues
        if blocks[i] == current:
            current_len += 1
        # The block ended, time to find it a home
        else:
            # print("".join([str(x) for x in blocks]))
            start_pos = 0
            running_len = 0
            # Search from the left
            hit = False
            for j in range(left_most_empty, i + 2):
                # Hit an empty block, save it
                if blocks[j] == ".":
                    # Don't need to look where there is no space
                    if not hit:
                        hit = True
                        left_most_empty = j
                    # Save the start pos so we can insert into it later
                    if running_len == 0:
                        start_pos = j
                    running_len += 1
                # Found the end of a empty block
                elif running_len != 0:
                    # If it fits:
                    if running_len >= current_len:
                        for insert in range(start_pos, start_pos + current_len):
                            blocks[insert] = current

                        for remove in range(i + 1, i + 1 + current_len):
                            blocks[remove] = "."
                        break
                    else:  # Empty space didn't fit, reset len and move on to the next empty space
                        running_len = 0

            if left_most_empty > i:
                break
            if blocks[i] != ".":  # and not tested[blocks[i]]:
                current = blocks[i]
                current_len = 1
            else:
                current_len = 0

    answer = 0

    for i, x in enumerate(blocks):
        if type(x) is not str:
            answer += i * x

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
