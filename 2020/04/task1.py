required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
optional_fields = {'cid'}


def get_passport_data():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    raw_passport_data = [[]]
    for line in lines:
        if line:
            raw_passport_data[-1] += line.split(' ')
        else:
            raw_passport_data.append([])
    passport_data = []
    for raw_data in raw_passport_data:
        data = []
        for raw_dat in raw_data:
            split = raw_dat.split(':')
            data.append((split[0], split[1]))
        passport_data.append(dict(data))
    return passport_data


def main():
    passport_data = get_passport_data()
    total_valid = 0
    for passport in passport_data:
        if required_fields.issubset(set(passport.keys())):
            total_valid += 1
    print('Total Valid Passports: %d' % total_valid)


if __name__ == '__main__':
    main()
