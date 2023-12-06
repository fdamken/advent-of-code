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
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    solved_races = [_solve_race(time, distance) for time, distance in zip(times, distances)]
    print(math.prod(max_time - min_time + 1 for min_time, max_time in solved_races))


if __name__ == "__main__":
    main()
