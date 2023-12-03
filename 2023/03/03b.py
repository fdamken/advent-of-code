import math
from typing import Optional


def _read_schematic() -> list[str]:
    with open("input.txt", "r") as f:
        schematic = f.readlines()
    # pad all the lines with non-symbols
    schematic = [f".{row.strip()}.." for row in schematic]
    schematic.insert(0, "." * len(schematic[0]))
    schematic.append("." * len(schematic[0]))
    return schematic


def _get_number_at(schematic: list[str], row_idx: int, col_idx: int) -> Optional[tuple[int, set[tuple[int, int]]]]:
    if not schematic[row_idx][col_idx].isnumeric():
        return None
    result = ""
    checked_coordinates = set()
    for i in range(col_idx, -1, -1):
        if schematic[row_idx][i].isnumeric():
            result = schematic[row_idx][i] + result
            checked_coordinates.add((row_idx, i))
        else:
            break
    for i in range(col_idx + 1, len(schematic[row_idx])):
        if schematic[row_idx][i].isnumeric():
            result = result + schematic[row_idx][i]
            checked_coordinates.add((row_idx, i))
        else:
            break
    return int(result), checked_coordinates


def _find_adjacent_numbers(schematic: list[str], row_idx: int, col_idx: int) -> list[int]:
    result = []
    surrounding_coordinates = [
        (row_idx - 1, col_idx - 1),  # top left
        (row_idx - 1, col_idx),  # top
        (row_idx - 1, col_idx + 1),  # top right
        (row_idx, col_idx + 1),  # right
        (row_idx + 1, col_idx + 1),  # bottom right
        (row_idx + 1, col_idx),  # bottom
        (row_idx + 1, col_idx - 1),  # bottom left
        (row_idx, col_idx - 1),  # left
    ]
    checked_coordinates = set()
    for row, col in surrounding_coordinates:
        if (row, col) in checked_coordinates:
            continue
        local_result = _get_number_at(schematic, row, col)
        if local_result is not None:
            number, local_checked_coordinates = local_result
            result.append(number)
            checked_coordinates |= local_checked_coordinates
    return result


def main():
    schematic = _read_schematic()
    result = 0
    for row_idx, row in enumerate(schematic[1:-1], start=1):
        for col_idx, item in enumerate(row[1:-1], start=1):
            if item == "*":
                adjacent_numbers = _find_adjacent_numbers(schematic, row_idx, col_idx)
                if len(adjacent_numbers) == 2:
                    result += math.prod(adjacent_numbers)
    print(result)


if __name__ == '__main__':
    main()
