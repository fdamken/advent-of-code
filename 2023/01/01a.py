def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    calibration_values = []
    for line in lines:
        numerics = [c for c in line if c.isnumeric()]
        calibration_values.append(int(numerics[0] + numerics[-1]))
    print(sum(calibration_values))


if __name__ == '__main__':
    main()
