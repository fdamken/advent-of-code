import re


def read_instructions():
    pattern = re.compile('^([NSEWLRF])(\d+)$')
    with open('input.txt') as f:
        lines = f.read().splitlines()
    instructions = []
    for line in (lines):
        action, arg = pattern.match(line).groups()
        instructions.append((action, int(arg)))
    return instructions


def main():
    instructions = read_instructions()
    x, y, rot = 0, 0, 90
    for action, arg in instructions:
        if action == 'F':
            if rot == 0:
                action = 'N'
            elif rot == 180:
                action = 'S'
            elif rot == 90:
                action = 'E'
            elif rot == 270:
                action = 'W'
            else:
                assert False, f'Unknown rotattion {rot}!'
        if action == 'N':
            y += arg
        elif action == 'S':
            y -= arg
        elif action == 'E':
            x += arg
        elif action == 'W':
            x -= arg
        elif action == 'L':
            rot = (rot - arg) % 360
        elif action == 'R':
            rot = (rot + arg) % 360
        else:
            assert False, f'Unknown action {action}!'

    manhattan_distance = abs(x) + abs(y)
    print('Manhattan Distance: %d' % manhattan_distance)


if __name__ == '__main__':
    main()
