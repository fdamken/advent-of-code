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

    print('Max. Seat ID: %d' % max(seat_ids))


if __name__ == '__main__':
    main()
