import re
from dataclasses import dataclass

ZERO_MATCH = re.match(r"(.)", "0")


@dataclass(frozen=True)
class BallSet:
    num_red: int
    num_green: int
    num_blue: int

    def __lt__(self, other) -> bool:
        return self <= other and self != other

    def __gt__(self, other) -> bool:
        return self >= other and self != other

    def __le__(self, other) -> bool:
        return self.num_red <= other.num_red and self.num_green <= other.num_green and self.num_blue <= other.num_blue

    def __ge__(self, other) -> bool:
        return self.num_red >= other.num_red and self.num_green >= other.num_green and self.num_blue >= other.num_blue


@dataclass(frozen=True)
class Game:
    idx: int
    ball_sets: list[BallSet]

    @property
    def minimum_ball_set(self) -> BallSet:
        return BallSet(
            max(ball_set.num_red for ball_set in self.ball_sets),
            max(ball_set.num_green for ball_set in self.ball_sets),
            max(ball_set.num_blue for ball_set in self.ball_sets),
        )


def _parse_line(line) -> Game:
    game_str, ball_sets_str = line.split(":")
    game_id = int(re.match(r"Game (\d+)", game_str).group(1))
    ball_sets = []
    for ball_set_str in ball_sets_str.split(";"):
        num_red = num_green = num_blue = 0
        for ball_str in ball_set_str.split(","):
            num, color = ball_str.strip().split(" ")
            if color == "red":
                num_red = int(num)
            elif color == "green":
                num_green = int(num)
            elif color == "blue":
                num_blue = int(num)
            else:
                assert False, "this should never happen"
        ball_sets.append(BallSet(num_red, num_green, num_blue))
    return Game(game_id, ball_sets)


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    games = [_parse_line(line) for line in lines]
    minimum_ball_sets = [game.minimum_ball_set for game in games]
    print(sum(ball_set.num_red * ball_set.num_green * ball_set.num_blue for ball_set in minimum_ball_sets))


if __name__ == '__main__':
    main()
