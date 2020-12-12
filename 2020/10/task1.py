import numpy as np


def main():
    data = np.loadtxt('input.txt', dtype=np.int)
    data.sort()
    jolt_differences = np.concatenate([data, [data[-1] + 3]]) - np.concatenate([[0], data])
    if (jolt_differences < 0).any() or (jolt_differences > 3).any():
        assert False, 'Jolt difference lower than zero or higher than three found!'
    no_1_difference = np.count_nonzero(jolt_differences == 1)
    no_2_difference = np.count_nonzero(jolt_differences == 2)
    no_3_difference = np.count_nonzero(jolt_differences == 3)
    print('Number of 1 Difference: %d' % no_1_difference)
    print('Number of 2 Difference: %d' % no_2_difference)
    print('Number of 3 Difference: %d' % no_3_difference)
    print('Result: %d' % (no_1_difference * no_3_difference))


if __name__ == '__main__':
    main()
