def main():
    with open('input.txt') as f:
        x = 0
        tree_hits = 0
        for line in f.read().splitlines()[1:]:
            x = (x + 3) % len(line)
            if line[x] == '#':
                tree_hits += 1
        print('Total Tree Hits: %d' % tree_hits)


if __name__ == '__main__':
    main()
