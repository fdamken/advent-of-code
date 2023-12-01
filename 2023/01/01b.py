import re


DIGITS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    calibration_values = []
    for line in lines:
        numerics = []
        for i in range(len(line)):
            match = re.search(f"({"|".join(DIGITS.keys())})", line[i:])
            if match:
                numerics.append(match.group(1))
        calibration_values.append(int(DIGITS[numerics[0]] + DIGITS[numerics[-1]]))
    print(sum(calibration_values))


if __name__ == '__main__':
    main()
