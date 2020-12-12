from copy import deepcopy


def read_input():
    with open('input.txt') as f:
        return [[char for char in line] for line in f.read().splitlines()]


def get_item_if_valid(state, y, x):
    if not (0 <= y < len(state) and 0 <= x < len(state[0])):
        return None
    return state[y][x]


def count_occupied(state, y, x):
    occupation_states = [
        get_item_if_valid(state, y, x - 1),
        get_item_if_valid(state, y, x + 1),
        get_item_if_valid(state, y - 1, x),
        get_item_if_valid(state, y + 1, x),
        get_item_if_valid(state, y - 1, x - 1),
        get_item_if_valid(state, y - 1, x + 1),
        get_item_if_valid(state, y + 1, x - 1),
        get_item_if_valid(state, y + 1, x + 1)
    ]
    return len([seat for seat in occupation_states if seat == '#'])


def step(state):
    next_state = deepcopy(state)
    for y in range(len(state)):
        for x in range(len(state[0])):
            seat = state[y][x]
            if seat == '.':
                continue
            occupied = count_occupied(state, y, x)
            if seat == 'L' and occupied == 0:
                next_state[y][x] = '#'
            if seat == '#' and occupied >= 4:
                next_state[y][x] = 'L'
    return next_state


def main():
    input = read_input()

    state = deepcopy(input)
    previous_state = None
    while previous_state is None or state != previous_state:
        previous_state = state
        state = step(previous_state)
    occupied = 0
    for row in state:
        for seat in row:
            if seat == '#':
                occupied += 1
    print('Occupied Seats after Convergence: %d' % occupied)


if __name__ == '__main__':
    main()
