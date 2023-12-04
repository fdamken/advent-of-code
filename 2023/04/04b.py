from dataclasses import dataclass, field


@dataclass
class Card:
    number: int
    winning_numbers: set[int]
    my_numbers: list[int]
    copies: int = 1
    matches: int = field(init=False)

    def __post_init__(self):
        self.matches = sum(1 for num in self.my_numbers if num in self.winning_numbers)


def _read_cards() -> list[Card]:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    cards = []
    for line in lines:
        card_str, numbers_str = line.split(":")
        card_number = int(card_str.strip().split()[1])
        winning_numbers_str, my_numbers_str = numbers_str.split("|")
        winning_numbers = {int(num) for num in winning_numbers_str.strip().split()}
        my_numbers = [int(num) for num in my_numbers_str.strip().split()]
        cards.append(Card(card_number, winning_numbers, my_numbers))
    return cards


def main() -> None:
    cards = _read_cards()
    for i, card in enumerate(cards):
        for next_card in cards[i + 1:i + 1 + card.matches]:
            next_card.copies += card.copies
    print(sum(card.copies for card in cards))


if __name__ == '__main__':
    main()
