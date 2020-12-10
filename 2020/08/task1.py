import re


def read_input():
    pattern = re.compile('^(acc|jmp|nop) ([+-]\d+)$')
    with open('input.txt') as f:
        lines = f.read().splitlines()
    ops = []
    for line in lines:
        op, arg = pattern.match(line).groups()
        ops.append((op, int(arg)))
    return ops


def main():
    ops = read_input()
    accumulator = 0
    instruction_pointer_history = []
    instruction_pointer = 0
    while True:
        if instruction_pointer in instruction_pointer_history:
            print('Detected an infinite loop!')
            break
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
    print('Accumulator Value: %d' % accumulator)


if __name__ == '__main__':
    main()
