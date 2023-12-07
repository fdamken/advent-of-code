from dataclasses import dataclass
from enum import Enum


class Card(Enum):
    CARD_J = 1
    CARD_2 = 2
    CARD_3 = 3
    CARD_4 = 4
    CARD_5 = 5
    CARD_6 = 6
    CARD_7 = 7
    CARD_8 = 8
    CARD_9 = 9
    CARD_T = 10
    CARD_Q = 11
    CARD_K = 12
    CARD_A = 13

    @staticmethod
    def from_str(card_str: str) -> "Card":
        return {
            "2": Card.CARD_2,
            "3": Card.CARD_3,
            "4": Card.CARD_4,
            "5": Card.CARD_5,
            "6": Card.CARD_6,
            "7": Card.CARD_7,
            "8": Card.CARD_8,
            "9": Card.CARD_9,
            "T": Card.CARD_T,
            "J": Card.CARD_J,
            "Q": Card.CARD_Q,
            "K": Card.CARD_K,
            "A": Card.CARD_A,
        }[card_str]

    def __eq__(self, other) -> bool:
        return self.compare(other) == 0

    def __ge__(self, other) -> bool:
        return self.compare(other) >= 0

    def __gt__(self, other) -> bool:
        return self.compare(other) > 0

    def __hash__(self):
        return self.value

    def __le__(self, other) -> bool:
        return self.compare(other) <= 0

    def __lt__(self, other) -> bool:
        return self.compare(other) < 0

    def __ne__(self, other) -> bool:
        return self.compare(other) != 0

    def __str__(self) -> str:
        return {
            Card.CARD_2: "2",
            Card.CARD_3: "3",
            Card.CARD_4: "4",
            Card.CARD_5: "5",
            Card.CARD_6: "6",
            Card.CARD_7: "7",
            Card.CARD_8: "8",
            Card.CARD_9: "9",
            Card.CARD_T: "T",
            Card.CARD_J: "J",
            Card.CARD_Q: "Q",
            Card.CARD_K: "K",
            Card.CARD_A: "A",
        }[self]

    def compare(self, other) -> int:
        return self.value - other.value


class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    @staticmethod
    def identify(hand: tuple[Card, Card, Card, Card, Card]) -> "HandType":
        if Card.CARD_J in hand:
            possible_hand_types = []
            hand_list = list(hand)
            joker_index = hand_list.index(Card.CARD_J)
            for card in [
                Card.CARD_2,
                Card.CARD_3,
                Card.CARD_4,
                Card.CARD_5,
                Card.CARD_6,
                Card.CARD_7,
                Card.CARD_8,
                Card.CARD_9,
                Card.CARD_T,
                Card.CARD_Q,
                Card.CARD_K,
                Card.CARD_A,
            ]:
                hand_list[joker_index] = card
                # noinspection PyTypeChecker
                possible_hand_types.append(HandType.identify(tuple(hand_list)))
            return max(possible_hand_types)

        hand_dict = {}
        for card in hand:
            hand_dict[card] = 1 + (hand_dict[card] if card in hand_dict else 0)
        hand_dict_values = list(sorted(hand_dict.values()))
        if hand_dict_values == [5]:
            return HandType.FIVE_OF_A_KIND
        if hand_dict_values == [2, 3]:
            return HandType.FULL_HOUSE
        if hand_dict_values == [1, 4]:
            return HandType.FOUR_OF_A_KIND
        if hand_dict_values == [1, 1, 3]:
            return HandType.THREE_OF_A_KIND
        if hand_dict_values == [1, 2, 2]:
            return HandType.TWO_PAIR
        if hand_dict_values == [1, 1, 1, 2]:
            return HandType.PAIR
        if hand_dict_values == [1, 1, 1, 1, 1]:
            return HandType.HIGH_CARD
        assert False, f"this should never happen, {hand_dict_values}"

    def __eq__(self, other) -> bool:
        return self.compare(other) == 0

    def __ge__(self, other) -> bool:
        return self.compare(other) >= 0

    def __gt__(self, other) -> bool:
        return self.compare(other) > 0

    def __le__(self, other) -> bool:
        return self.compare(other) <= 0

    def __lt__(self, other) -> bool:
        return self.compare(other) < 0

    def __ne__(self, other) -> bool:
        return self.compare(other) != 0

    def compare(self, other) -> int:
        return self.value - other.value


@dataclass(frozen=True)
class Hand:
    cards: tuple[Card, Card, Card, Card, Card]

    @staticmethod
    def from_str(hand_str: str) -> "Hand":
        cards = tuple(Card.from_str(card_str) for card_str in hand_str)
        assert len(cards) == 5
        # noinspection PyTypeChecker
        return Hand(cards)

    def __eq__(self, other) -> bool:
        return self.compare(other) == 0

    def __ge__(self, other) -> bool:
        return self.compare(other) >= 0

    def __gt__(self, other) -> bool:
        return self.compare(other) > 0

    def __le__(self, other) -> bool:
        return self.compare(other) <= 0

    def __lt__(self, other) -> bool:
        return self.compare(other) < 0

    def __ne__(self, other) -> bool:
        return self.compare(other) != 0

    def __str__(self) -> str:
        return f"{"".join(str(card) for card in self.cards)} ({HandType.identify(self.cards)})"

    def compare(self, other) -> int:
        self_type = HandType.identify(self.cards)
        other_type = HandType.identify(other.cards)
        result = self_type.compare(other_type)
        if result == 0:
            if self.cards < other.cards:
                result = -1
            elif self.cards > other.cards:
                result = 1
            else:
                result = 0
        return result


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    hands = [Hand.from_str(line.split()[0]) for line in lines]
    bids = [int(line.split()[1]) for line in lines]
    ordered_hands_bits = list(sorted(zip(hands, bids), key=lambda x: x[0]))
    result = 0
    for i, (_, bid) in enumerate(ordered_hands_bits, start=1):
        result += i * bid
    print(result)


if __name__ == '__main__':
    main()
