def main() -> None:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    result = 0
    for line in lines:
        winning_numbers_str, my_numbers_str = line.split(":")[1].split("|")
        winning_numbers = {int(num) for num in winning_numbers_str.strip().split()}
        my_numbers = [int(num) for num in my_numbers_str.strip().split()]
        matches = sum(1 for num in my_numbers if num in winning_numbers)
        if matches > 0:
            result += 2 ** (matches - 1)
    print(result)


if __name__ == '__main__':
    main()
