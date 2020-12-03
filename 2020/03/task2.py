def traverse_slope(lines, slope_right, slope_down):
    x = 0
    tree_hits = 0
    for line in lines[slope_down::slope_down]:
        x = (x + slope_right) % len(line)
        if line[x] == '#':
            tree_hits += 1
    return tree_hits


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_hits_product = 1
    for slope_right, slope_down in slopes:
        tree_hits = traverse_slope(lines, slope_right, slope_down)
        tree_hits_product *= tree_hits
        print('Right %d, Down %d; Total Tree Hits: %d' % (slope_right, slope_down, tree_hits))
    print('Total Tree Hits Product: %d' % tree_hits_product)


if __name__ == '__main__':
    main()
