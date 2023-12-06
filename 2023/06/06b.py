import math


def _solve_race(time: int, distance: int) -> tuple[int, int]:
    # find the minimum time\
    min_time = 0
    for min_time in range(0, time + 1):
        if min_time * (time - min_time) > distance:
            break
    max_time = time
    for max_time in range(time, -1, -1):
        if max_time * (time - max_time) > distance:
            break
    return min_time, max_time


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    min_time, max_time = _solve_race(time, distance)
    print(max_time - min_time + 1)


if __name__ == "__main__":
    main()
