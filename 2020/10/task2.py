import numpy as np


def main():
    data = np.loadtxt('input.txt', dtype=np.int)
    data.sort()
    total = 1
    group = 0
    group_size = 0
    for i in range(-1, len(data)):
        if i == len(data) - 1:
            successors = 1
        else:
            if i == -1:
                joltage = 0
            else:
                joltage = data[i]
            successors = np.count_nonzero(data[i + 1:i + 1 + 3] - joltage <= 3)
        if successors == 1:
            if group_size == 1:
                total *= group
            elif group_size >= 2:
                total *= group - 1
            group = 0
            group_size = 0
        else:
            group += successors
            group_size += 1
    print('Total Number of Combinations: %d' % total)


if __name__ == '__main__':
    main()
