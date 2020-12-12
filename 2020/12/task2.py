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
    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1
    for action, arg in instructions:
        if action == 'N':
            waypoint_y += arg
        elif action == 'S':
            waypoint_y -= arg
        elif action == 'E':
            waypoint_x += arg
        elif action == 'W':
            waypoint_x -= arg
        elif action == 'L':
            while arg > 0:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
                arg -= 90
        elif action == 'R':
            while arg > 0:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
                arg -= 90
        elif action == 'F':
            ship_x += waypoint_x * arg
            ship_y += waypoint_y * arg
        else:
            assert False, f'Unknown action {action}!'

    manhattan_distance = abs(ship_x) + abs(ship_y)
    print('Manhattan Distance: %d' % manhattan_distance)


if __name__ == '__main__':
    main()
