def _read_schematic() -> list[str]:
    with open("input.txt", "r") as f:
        schematic = f.readlines()
    # pad all the lines with non-symbols
    schematic = [f".{row.strip()}.." for row in schematic]  # pad with two dots on the right to make sure every number is added (line 40)
    schematic.insert(0, "." * len(schematic[0]))
    schematic.append("." * len(schematic[0]))
    return schematic


def _is_symbol(item: str) -> bool:
    return not item.isnumeric() and item != "."


def _is_adjacent_to_symbol(schematic: list[str], row_idx: int, col_idx: int) -> bool:
    return any(
        _is_symbol(schematic[row][col]) for row, col in [
            (row_idx - 1, col_idx - 1),  # top left
            (row_idx - 1, col_idx),  # top
            (row_idx - 1, col_idx + 1),  # top right
            (row_idx, col_idx + 1),  # right
            (row_idx + 1, col_idx + 1),  # bottom right
            (row_idx + 1, col_idx),  # bottom
            (row_idx + 1, col_idx - 1),  # bottom left
            (row_idx, col_idx - 1),  # left
        ]
    )


def main():
    schematic = _read_schematic()
    result = 0
    for row_idx, row in enumerate(schematic[1:-1], start=1):
        current_num = ""
        is_adjacent_to_symbol = False
        for col_idx, item in enumerate(row[1:-1], start=1):
            if item.isnumeric():
                current_num += item
                is_adjacent_to_symbol |= _is_adjacent_to_symbol(schematic, row_idx, col_idx)
            else:
                if current_num.isnumeric():
                    if is_adjacent_to_symbol:
                        result += int(current_num)
                    else:
                        print(f"Found a number that is not adjacent to a symbol: {current_num} ({row_idx}, {col_idx})")
                current_num = ""
                is_adjacent_to_symbol = False
    print(result)


if __name__ == '__main__':
    main()
