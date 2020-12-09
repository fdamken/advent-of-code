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


def get_bags_containing(rules, base_bag_color):
    visited = set()
    todo = {base_bag_color}
    while len(todo) > 0:
        current_bag_color = todo.pop()
        visited.add(current_bag_color)
        for bag_color, contains_bags in rules:
            if any([x[1] == current_bag_color for x in contains_bags]):
                if bag_color not in visited:
                    todo.add(bag_color)
    return visited - {base_bag_color}


def main():
    rules = parse_input()
    bags_containing_shiny_gold = get_bags_containing(rules, 'shiny gold')
    print('Number of Bags: %d' % len(bags_containing_shiny_gold))


if __name__ == '__main__':
    main()
