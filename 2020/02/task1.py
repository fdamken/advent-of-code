import re


def count_occurrences(string, letter):
    occurrences = 0
    for c in string:
        if c == letter:
            occurrences += 1
    return occurrences


def main():
    pattern = re.compile('^(\d+)-(\d+) (\w): (\w+)$')
    with open('input.txt') as f:
        valid_count = 0
        for line in f.readlines():
            match = pattern.match(line)
            letter_min, letter_max, letter, string = match.groups()
            letter_min = int(letter_min)
            letter_max = int(letter_max)
            if letter_min <= count_occurrences(string, letter) <= letter_max:
                valid_count += 1
        print('Number of valid password: %d' % valid_count)


if __name__ == '__main__':
    main()
