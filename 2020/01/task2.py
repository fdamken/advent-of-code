import numpy as np


def main():
    input = np.loadtxt('input.txt', dtype=np.int)
    for i, ie in enumerate(input):
        for j, je in enumerate(input[i:]):
            for k, ke in enumerate(input[j:]):
                if ie + je + ke == 2020:
                    result = ie * je * ke
                    print('%d + %d + %d = 2020' % (ie, je, ke))
                    print('%d * %d * %d = %d' % (ie, je, ke, result))
                    return


if __name__ == '__main__':
    main()
