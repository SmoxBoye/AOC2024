# Pre-thoughts: "unholy parsing moment"
# Regex moment? This is 100% gonna bite me in part 2 but im committing yolo.


import re


def part1():
    with open("data.txt", "r") as f:
        file = f.read()

    # Find all valid mul
    mul = re.findall("mul\(\d{1,3},\d{1,3}\)", file)

    # Get the numbers
    mul = [re.search("\d{1,3},\d{1,3}", x).group(0) for x in mul]  #

    # Make them actual int pairs lmao
    mul = [list(map(int, x.split(","))) for x in mul]

    result = 0

    for pair in mul:
        result += pair[0] * pair[1]

    print(result)


# It has come to my attention that regex is op and it literally just works
def part2():
    with open("data.txt", "r") as f:
        file = f.read()

    # Plan: Literally just delete all the stuff between don't() and do() lmao

    do = True  # It is implied that it begins with do

    filtered_file = []

    for i in range(len(file)):
        if file[i : i + 7] == "don't()":
            do = False
        if file[i : i + 4] == "do()":
            do = True

        if do:
            filtered_file.append(file[i])

    filtered_file = "".join(filtered_file)

    # And part1 here we go!

    # Find all valid mul
    mul = re.findall("mul\(\d{1,3},\d{1,3}\)", filtered_file)

    # Get the numbers
    mul = [re.search("\d{1,3},\d{1,3}", x).group(0) for x in mul]  #

    # Make them actual int pairs lmao
    mul = [list(map(int, x.split(","))) for x in mul]

    result = 0

    for pair in mul:
        result += pair[0] * pair[1]

    print(result)


# Afterword: This is straight up the first time i've used regex in forever (no LLM)
# Im actually surprised how well it went


if __name__ == "__main__":
    part1()
    part2()
