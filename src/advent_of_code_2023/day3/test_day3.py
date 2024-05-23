from advent_of_code_2023.day3.solution import part_1, part_2

test_input = """467..114..
                    ...*......
                    ..35..633.
                    ......#...
                    617*......
                    .....+.58.
                    ..592.....
                    ......755.
                    ...$.*....
                    .664.598.."""

lines = [line.strip() for line in test_input.splitlines()]
grid = [[column for column in line] for line in lines]

def test_parse_numbers():
    res = part_1(grid)
    assert res == 4361


def test_part_2_grid():
    res = part_2(grid)

    assert res == 467835
