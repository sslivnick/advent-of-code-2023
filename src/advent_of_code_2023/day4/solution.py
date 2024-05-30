from collections import defaultdict


def parse_number_str(number_str: str) -> set[str]:
    return set(filter(lambda s: s != "", number_str.strip().split(" ")))


def parse_cards(lines: list[str]) -> list[tuple[set[str], set[str]]]:
    games = []
    for line in lines:
        _, numbers = line.split(":")
        have, winning = numbers.split("|")
        have = parse_number_str(have)
        winning = parse_number_str(winning)
        games.append((have, winning))
    return games


def part_1(lines: list[str]):
    parsed_games = parse_cards(lines)
    score = 0
    for game in parsed_games:
        winning_numbers = game[0].intersection(game[1])
        num_winning = len(winning_numbers)

        if num_winning > 0:
            points = 1
            for _ in range(num_winning - 1):
                points *= 2
            score += points
    return score


def part_2(lines: list[str]):
    parsed_games = parse_cards(lines)
    cards = defaultdict(int)
    for card_number, game in enumerate(parsed_games, 1):
        winning_numbers = len(game[0].intersection(game[1]))
        cards[card_number] += 1

        for card in range(winning_numbers):
            idx = card_number + card + 1
            cards[idx] += cards[card_number]
    return sum(cards.values())


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    res = part_1(lines)
    print(f"result for part 1 is {res}")

    res = part_2(lines)
    print(f"result for part 2 is {res}")
