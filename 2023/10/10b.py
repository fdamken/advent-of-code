from copy import deepcopy
from dataclasses import dataclass
from typing import Optional

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm


def _connects_to_above(tile: str) -> bool:
    return tile in ("│", "┘", "└")


def _connects_to_below(tile: str) -> bool:
    return tile in ("│", "┐", "┌")


def _connects_to_left(tile: str) -> bool:
    return tile in ("─", "┘", "┐")


def _connects_to_right(tile: str) -> bool:
    return tile in ("─", "└", "┌")


def _get_surrounding_tiles(lines: list[str], x: int, y: int) \
        -> tuple[tuple[tuple[int, int], str], tuple[tuple[int, int], str], tuple[tuple[int, int], str], tuple[tuple[int, int], str]]:
    return (
        ((x, y - 1), lines[y - 1][x]),
        ((x, y + 1), lines[y + 1][x]),
        ((x - 1, y), lines[y][x - 1]),
        ((x + 1, y), lines[y][x + 1]),
    )


def _get_next_tile(lines: list[str], current_x: int, current_y: int, previous_x: Optional[int], previous_y: Optional[int]) -> tuple[int, int]:
    current_tile = lines[current_y][current_x]
    previous_coordinates = (previous_x, previous_y)
    (above_coordinates, above_tile), (below_coordinates, below_tile), (left_coordinates, left_tile), (right_coordinates, right_tile) = _get_surrounding_tiles(
        lines,
        current_x,
        current_y
    )
    if above_coordinates != previous_coordinates and _connects_to_above(current_tile) and _connects_to_below(above_tile):
        return above_coordinates
    if below_coordinates != previous_coordinates and _connects_to_below(current_tile) and _connects_to_above(below_tile):
        return below_coordinates
    if left_coordinates != previous_coordinates and _connects_to_left(current_tile) and _connects_to_right(left_tile):
        return left_coordinates
    if right_coordinates != previous_coordinates and _connects_to_right(current_tile) and _connects_to_left(right_tile):
        return right_coordinates
    assert False, f"could not find next tile at ({current_x}, {current_y})"


def _follow_path(lines: list[str], start_x: int, start_y: int) -> list[tuple[int, int]]:
    path = [(start_x, start_y)]
    while True:
        path.append(_get_next_tile(lines, *path[-1], *(path[-2] if len(path) > 1 else (None, None))))
        if path[-1] == (start_x, start_y):
            break
    return path[:-1]


def _pad(lines: list[str]) -> list[str]:
    lines = [f"..{line}.." for line in lines]
    lines.insert(0, "." * len(lines[0]))
    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))
    lines.append("." * len(lines[0]))
    return lines


def _replace_with_unicode(s: str) -> str:
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    return s \
        .replace("|", "│") \
        .replace("-", "─") \
        .replace("L", "└") \
        .replace("J", "┘") \
        .replace("7", "┐") \
        .replace("F", "┌") \
        .replace(".", " ") \
        .replace("S", "┼")


def _find_and_fix_starting_tile(lines: list[str]) -> tuple[[int, int], list[str]]:
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "┼":
                (_, tile_above), (_, tile_below), (_, tile_left), (_, tile_right) = _get_surrounding_tiles(lines, x, y)
                match (
                    _connects_to_below(tile_above),
                    _connects_to_above(tile_below),
                    _connects_to_right(tile_left),
                    _connects_to_left(tile_right),
                ):
                    case (True, True, False, False):
                        new_tile = "│"
                    case (False, False, True, True):
                        new_tile = "─"
                    case (True, False, False, True):
                        new_tile = "└"
                    case (True, False, True, False):
                        new_tile = "┘"
                    case (False, True, True, False):
                        new_tile = "┐"
                    case (False, True, False, True):
                        new_tile = "┌"
                    case _:
                        assert False, f"unexpected tile configuration at ({x}, {y}): {tile_above}, {tile_below}, {tile_left}, {tile_right}"
                lines[y] = lines[y][:x] + new_tile + lines[y][x + 1:]
                return (x, y), lines
    assert False, "could not find starting tile"


def _remove_non_loop_tiles(lines: list[str], path: list[tuple[int, int]]) -> list[str]:
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            lines[y] = lines[y][:x] + (" " if (x, y) not in path else c) + lines[y][x + 1:]
    return lines


def _format_infections(infections: list[list[int]]) -> list[str]:
    result = []
    for infections_row in infections:
        row = []
        for infection in infections_row:
            match infection:
                case 0b0000:
                    row.append(" ")
                case 0b0001:
                    row.append("\u2597")
                case 0b0010:
                    row.append("\u2596")
                case 0b0011:
                    row.append("\u2584")
                case 0b0100:
                    row.append("\u259d")
                case 0b0101:
                    row.append("\u2590")
                case 0b0110:
                    row.append("\u259e")
                case 0b0111:
                    row.append("\u259f")
                case 0b1000:
                    row.append("\u2598")
                case 0b1001:
                    row.append("\u259a")
                case 0b1010:
                    row.append("\u258c")
                case 0b1011:
                    row.append("\u2599")
                case 0b1100:
                    row.append("\u2580")
                case 0b1101:
                    row.append("\u259c")
                case 0b1110:
                    row.append("\u259b")
                case 0b1111:
                    row.append("\u2588")
                case _:
                    assert False, f"unexpected infection: {infection}"
        result.append("".join(row))
    return result


def _tick_infections(infections: list[list[int]], lines: list[str]) -> bool:
    old_infections = deepcopy(infections)
    for y, infections_row in enumerate(old_infections[1:-1], start=1):
        for x, infection in enumerate(infections_row[1:-1], start=1):
            if infection != 0:
                # already infected, this does not spread further
                continue
            (above_coordinates, above_tile), (below_coordinates, below_tile), (left_coordinates, left_tile), (right_coordinates, right_tile) = _get_surrounding_tiles(lines, x, y)
            above_infection = old_infections[above_coordinates[1]][above_coordinates[0]]
            below_infection = old_infections[below_coordinates[1]][below_coordinates[0]]
            left_infection = old_infections[left_coordinates[1]][left_coordinates[0]]
            right_infection = old_infections[right_coordinates[1]][right_coordinates[0]]

            # first spread the infection towards the new tile
            if above_infection & 0b0010 != 0:
                # infection from above left
                infection |= 0b1000
            if above_infection & 0b0001 != 0:
                # infection from above right
                infection |= 0b0100
            if below_infection & 0b1000 != 0:
                # infection from below left
                infection |= 0b0010
            if below_infection & 0b0100 != 0:
                # infection from below right
                infection |= 0b0001
            if left_infection & 0b0100 != 0:
                # infection from left top
                infection |= 0b1000
            if left_infection & 0b0001 != 0:
                # infection from left bottom
                infection |= 0b0010
            if right_infection & 0b1000 != 0:
                # infection from right top
                infection |= 0b0100
            if right_infection & 0b0010 != 0:
                # infection from right bottom
                infection |= 0b0001

            # and then distribute it on that tile
            match lines[y][x]:
                case "│":
                    if infection & 0b1000 != 0 or infection & 0b0010 != 0:
                        # completely infect left
                        infection |= 0b1010
                    if infection & 0b0100 != 0 or infection & 0b0001 != 0:
                        # completely infect right
                        infection |= 0b0101
                case "─":
                    if infection & 0b1000 != 0 or infection & 0b0100 != 0:
                        # completely infect top
                        infection |= 0b1100
                    if infection & 0b0010 != 0 or infection & 0b0001 != 0:
                        # completely infect bottom
                        infection |= 0b0011
                case "└":
                    if infection & 0b1000 != 0 or infection & 0b0010 != 0 or infection & 0b0001 != 0:
                        # completely infect bottom left corner
                        infection |= 0b1011
                case "┘":
                    if infection & 0b0100 != 0 or infection & 0b0010 != 0 or infection & 0b0001 != 0:
                        # completely infect bottom right corner
                        infection |= 0b0111
                case "┐":
                    if infection & 0b1000 != 0 or infection & 0b0100 != 0 or infection & 0b0001 != 0:
                        # completely infect top right corner
                        infection |= 0b1101
                case "┌":
                    if infection & 0b1000 != 0 or infection & 0b0100 != 0 or infection & 0b0010 != 0:
                        # completely infect top left corner
                        infection |= 0b1110
                case " ":
                    if infection != 0:
                        # completely infect
                        infection |= 0b1111
                case _:
                    assert False
            infections[y][x] = infection
    return infections != old_infections


def _simulation_infections(lines: list[str]) -> list[str]:
    infections = [[0b1111] + [0] * (len(line) - 2) + [0b1111] for line in lines]
    infections[0] = [0b1111] * len(infections[0])
    infections[-1] = [0b1111] * len(infections[-1])

    while _tick_infections(infections, lines):
        pass
    return _format_infections(infections)


def main() -> None:
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    lines = _pad(lines)
    lines = [_replace_with_unicode(line) for line in lines]
    (start_x, start_y), lines = _find_and_fix_starting_tile(lines)
    path = _follow_path(lines, start_x, start_y)
    lines = _remove_non_loop_tiles(lines, path)
    infections = _simulation_infections(lines)
    num_uninfected_tiles = ("".join(infections)).count(" ")
    print(num_uninfected_tiles)


if __name__ == "__main__":
    main()
