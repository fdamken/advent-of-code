import re


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    instructions = lines[0].strip()
    nodes = {}
    for line in lines[2:]:
        node, node_left, node_right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
        nodes[node] = {"L": node_left, "R": node_right}
    history = ["AAA"]
    instruction_idx = 0
    while history[-1] != "ZZZ":
        current_node = history[-1]
        history.append(nodes[current_node][instructions[instruction_idx]])
        instruction_idx = (instruction_idx + 1) % len(instructions)
    print(len(history) - 1)


if __name__ == "__main__":
    main()
