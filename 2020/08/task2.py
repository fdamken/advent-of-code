import re
from copy import deepcopy


def read_input():
    pattern = re.compile('^(acc|jmp|nop) ([+-]\d+)$')
    with open('input.txt') as f:
        lines = f.read().splitlines()
    ops = []
    for line in lines:
        op, arg = pattern.match(line).groups()
        ops.append([op, int(arg)])
    return ops


def run(ops):
    accumulator = 0
    instruction_pointer_history = []
    instruction_pointer = 0
    while True:
        if instruction_pointer in instruction_pointer_history:
            return False, accumulator
        instruction_pointer_history.append(instruction_pointer)
        op, arg = ops[instruction_pointer]
        if op == 'acc':
            accumulator += arg
        elif op == 'jmp':
            instruction_pointer += arg - 1
        elif op == 'nop':
            pass
        else:
            assert False, f'Unknown operation {op}!'
        instruction_pointer += 1
        if instruction_pointer >= len(ops):
            break
    return True, accumulator


def main():
    unmodified_ops = read_input()
    for i in range(len(unmodified_ops)):
        ops = deepcopy(unmodified_ops)
        if ops[i][0] == 'jmp':
            ops[i][0] = 'nop'
        elif ops[i][0] == 'nop':
            ops[i][0] = 'jmp'
        else:
            continue
        terminates, accumulator = run(ops)
        if terminates:
            print('Changed Line %d, Accumulator Value: %d' % (i, accumulator))


if __name__ == '__main__':
    main()
