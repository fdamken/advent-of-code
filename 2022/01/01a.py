elves = []

current_sum = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line == "":
            elves.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)

print(max(elves))
