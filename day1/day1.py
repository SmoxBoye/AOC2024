def part1():
    with open("data.txt", "r") as f:
        data = f.readlines()
    left = []
    right = []
    for i in range(len(data)):
        row = data[i]
        row = row.rstrip()
        parts = row.split("  ")
        left.append(int(parts[0]))
        right.append(int(parts[1]))
    
    left.sort()
    right.sort()

    result = 0
    for row in zip(left, right):
        result += abs(row[0] - row[1]) 
    print(result)

def part2():
    with open("data.txt", "r") as f:
        data = f.readlines()
    left = []
    right = []
    for i in range(len(data)):
        row = data[i]
        row = row.rstrip()
        parts = row.split("  ")
        left.append(int(parts[0]))
        right.append(int(parts[1]))
    
    right_set = {}
    for row in right:
        if right_set.get(row) == None:
            right_set.update({row: 1})
        else: 
            right_set[row] += 1
    
    similarity_score = 0
    for row in left:
        val = right_set.get(row)
        if val == None:
            continue
        similarity_score += row * right_set[row]
    print(similarity_score)

if __name__ == "__main__":
    part1()
    part2()