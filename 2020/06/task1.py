def read_answers():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    answers = [[]]
    for line in lines:
        if line:
            answers[-1].append(line)
        else:
            answers.append([])
    return answers


def main():
    answers = read_answers()
    total_yes_answers = 0
    for group_answers in answers:
        yes_answers = set()
        for answer in group_answers:
            for char in answer:
                yes_answers.add(char)
        total_yes_answers += len(yes_answers)
    print('Total "yes" Answers: %d' % total_yes_answers)


if __name__ == '__main__':
    main()
