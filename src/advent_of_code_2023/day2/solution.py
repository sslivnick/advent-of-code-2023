from enum import Enum
from typing import Sequence


class Color(str, Enum):
    Blue = "blue"
    Red = "red"
    Green = "green"


class Game:
    def __init__(self, id: int) -> None:
        self.id = id
        self.blue = 0
        self.red = 0
        self.green = 0

    def add_color(self, color: Color, number: int):
        if color == Color.Blue:
            if number > self.blue:
                self.blue = number
        elif color == Color.Red:
            if number > self.red:
                self.red = number
        elif color == Color.Green:
            if number > self.green:
                self.green = number
        else:
            raise ValueError("invalid color")

    def __repr__(self) -> str:
        return f"id:{self.id}, blue:{self.blue}, red:{self.red}, green{self.green}"


def parse_input(lines: Sequence[str]) -> list[Game]:
    games = []
    for line in lines:
        game_id, color_counts = line.strip().split(":")
        id = int(game_id.split(" ")[1])
        game = Game(id)

        for attempt in color_counts.split(";"):
            reachs = attempt.split(",")
            for reach in reachs:
                count, color = reach.strip().split(" ")
                game.add_color(Color(color), int(count))

        games.append(game)
    return games


def part_1(games: list[Game]) -> int:
    return sum(game.id for game in games if game.red <= 12 and game.green <= 13 and game.blue <= 14)


def part_2(games: list[Game]) -> int:
    return sum(game.red * game.green * game.blue for game in games)


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    games = parse_input(lines)

    part_1_result = part_1(games)
    print(f"part 1 result is: {part_1_result}")

    part_2_result = part_2(games)
    print(f"part 2 result is: {part_2_result}")
