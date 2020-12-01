import numpy as np


def main():
    input = np.loadtxt('input.txt', dtype=np.int)
    for i, ie in enumerate(input):
        for j, je in enumerate(input[i:]):
            if ie + je == 2020:
                result = ie * je
                print('%d + %d = 2020' % (ie, je))
                print('%d * %d = %d' % (ie, je, result))
                return


if __name__ == '__main__':
    main()
