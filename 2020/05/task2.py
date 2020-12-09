def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    seat_ids = []
    for line in lines:
        row_identifier = line[:7]
        col_identifier = line[7:]

        row = 0
        for i, char in enumerate(reversed(row_identifier)):
            row += 2 ** i if char == 'B' else 0
        col = 0
        for i, char in enumerate(reversed(col_identifier)):
            col += 2 ** i if char == 'R' else 0
        seat_id = row * 8 + col
        seat_ids.append(seat_id)

    sorted_seat_ids = sorted(seat_ids)
    for prev, cur in zip(sorted_seat_ids[:-1], sorted_seat_ids[1:]):
        if prev + 2 == cur:
            print('My Seat ID: %d' % (prev + 1))


if __name__ == '__main__':
    main()
