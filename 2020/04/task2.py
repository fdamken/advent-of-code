import re

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


def is_passport_valid(passport):
    pattern_year = re.compile('^\d{4}$')
    pattern_hgt = re.compile('^(\d+)(cm|in)$')
    pattern_hcl = re.compile('^#([0-9a-f]{6})$')
    pattern_ecl = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
    pattern_pid = re.compile('^\d{9}$')

    if not required_fields.issubset(set(passport.keys())):
        return False
    byr_valid = pattern_year.match(passport['byr']) and (1920 <= int(passport['byr']) <= 2002)
    iyr_valid = pattern_year.match(passport['iyr']) and (2010 <= int(passport['iyr']) <= 2020)
    eyr_valid = pattern_year.match(passport['eyr']) and (2020 <= int(passport['eyr']) <= 2030)
    hgt_match = pattern_hgt.match(passport['hgt'])
    if hgt_match:
        value, unit = hgt_match.groups()
        value = int(value)
        if unit == 'cm':
            hgt_valid = (150 <= value <= 193)
        elif unit == 'in':
            hgt_valid = (59 <= value <= 76)
        else:
            hgt_valid = False
    else:
        hgt_valid = False
    hcl_valid = pattern_hcl.match(passport['hcl'])
    ecl_valid = pattern_ecl.match(passport['ecl'])
    pid_valid = pattern_pid.match(passport['pid'])
    return byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid


def main():
    passport_data = get_passport_data()
    total_valid = 0
    for passport in passport_data:
        if is_passport_valid(passport):
            total_valid += 1
    print('Total Valid Passports: %d' % total_valid)


if __name__ == '__main__':
    main()
