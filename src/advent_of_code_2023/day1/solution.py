def get_calibration_value_part_1(line: str) -> int:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    return int(digits[0] + digits[-1])


def part1(lines: list[str]):
    calibration_values = []
    for line in lines:
        res = get_calibration_value_part_1(line)
        calibration_values.append(res)
    return sum(calibration_values)


def get_calibration_value_part_2(line: str) -> int:
    string_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    matches = []
    for p in range(len(line)):
        slice = line[p:]
        for key, value in string_digits.items():
            if slice.startswith(key) or slice.startswith(value):
                matches.append(value)
    return int(matches[0] + matches[-1])


def part2(lines: list[str]):
    calibration_values = []
    for line in lines:
        res = get_calibration_value_part_2(line)
        calibration_values.append(res)

    return sum(calibration_values)


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    res = part1(lines)
    print(res)
    res = part2(lines)
    print(res)
