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
            letter_pos_1, letter_pos_2, letter, string = match.groups()
            letter_pos_1 = int(letter_pos_1)
            letter_pos_2 = int(letter_pos_2)
            if (string[letter_pos_1 - 1] == letter) != (string[letter_pos_2 - 1] == letter):  # This is an XOR.
                valid_count += 1
        print('Number of valid password: %d' % valid_count)


if __name__ == '__main__':
    main()
