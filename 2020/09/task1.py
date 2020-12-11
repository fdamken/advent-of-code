def contains_number_as_sum(n, numbers):
    for i, a in enumerate(numbers):
        for b in numbers[i + 1:]:
            if a != b and a + b == n:
                return True
    return False


def main():
    with open('input.txt') as f:
        numbers = [int(line) for line in f.read().splitlines()]
    for i in range(25, len(numbers)):
        if not contains_number_as_sum(numbers[i], numbers[i - 25:i]):
            print('First Invalid Number: %d' % numbers[i])


if __name__ == '__main__':
    main()
