import re


def parse_input():
    bag_pattern = re.compile('^ *(\d+) ([\w ]+) bags?[,.]? *$')
    with open('input.txt') as f:
        lines = f.read().splitlines()
    rules = []
    for line in lines:
        split = line.split('bags contain')
        bag_color = split[0].strip()
        contains_bags_raw = split[1].strip()
        contains_bags = []
        if contains_bags_raw != 'no other bags.':
            for bag in contains_bags_raw.split(','):
                quantity, color = bag_pattern.match(bag).groups()
                contains_bags.append((int(quantity), color.strip()))
        rules.append((bag_color, contains_bags))
    return rules


def count_contained_bags(rules, base_bag_color):
    for bag_color, contains_bags in rules:
        if bag_color == base_bag_color:
            total_count = 1
            for count, bag_color in contains_bags:
                total_count += count * count_contained_bags(rules, bag_color)
            return total_count



def main():
    rules = parse_input()
    contained_bags = count_contained_bags(rules, 'shiny gold') - 1
    print('Number of Bags Contained: %d' % contained_bags)


if __name__ == '__main__':
    main()
