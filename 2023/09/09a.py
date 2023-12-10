def _extrapolate(history: list[int]) -> int:
    if all(x == 0 for x in history):
        return 0
    return _extrapolate([y - x for x, y in zip(history[:-1], history[1:])]) + history[-1]


def main() -> None:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    histories = [[int(x) for x in line.split()] for line in lines]
    print(sum(_extrapolate(history) for history in histories))


if __name__ == "__main__":
    main()
