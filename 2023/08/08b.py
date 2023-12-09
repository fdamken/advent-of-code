import math
import re


def _run_instructions(instructions: str, node_mappings: dict[str, dict[str, str]], start_node: str) -> int:
    current_node = start_node
    instruction_idx = 0
    num_steps = 0
    while current_node[-1] != "Z":
        current_node = node_mappings[current_node][instructions[instruction_idx]]
        instruction_idx = (instruction_idx + 1) % len(instructions)
        num_steps += 1
    return num_steps


def main() -> None:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    instructions = lines[0].strip()
    node_mappings = {}
    for line in lines[2:]:
        node, node_left, node_right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
        node_mappings[node] = {"L": node_left, "R": node_right}
    print(math.lcm(*[_run_instructions(instructions, node_mappings, node) for node in node_mappings.keys() if node[-1] == "A"]))


if __name__ == "__main__":
    main()
