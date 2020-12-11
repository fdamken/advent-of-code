def contains_number_as_sum(n, numbers):
    for i, a in enumerate(numbers):
        for b in numbers[i + 1:]:
            if a != b and a + b == n:
                return True
    return False


def find_contiguous_set(n, numbers):
    for i, a in enumerate(numbers):
        sum = 0
        for j in range(i, len(numbers)):
            sum += numbers[j]
            if sum >= n:
                break
        if sum == n:
            # noinspection PyUnboundLocalVariable
            return numbers[i:j + 1]
    assert False, 'No contiguous set found!'


def main():
    with open('input.txt') as f:
        numbers = [int(line) for line in f.read().splitlines()]
    for i in range(25, len(numbers)):
        if not contains_number_as_sum(numbers[i], numbers[i - 25:i]):
            invalid_number = numbers[i]
            break
    # noinspection PyUnboundLocalVariable
    contiguous_set = find_contiguous_set(invalid_number, numbers)
    print('Encryption Weakness: %d' % (min(contiguous_set) + max(contiguous_set)))


if __name__ == '__main__':
    main()
