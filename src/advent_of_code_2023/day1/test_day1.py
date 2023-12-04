from advent_of_code_2023.day1.solution import part1, part2, get_calibration_value_part_1, get_calibration_value_part_2

part_1_inputs = {
        "1abc2": 12,
        "pqr3stu8vwx": 38,
        "a1b2c3d4e5f": 15,
        "treb7uchet": 77,
    }


def test_calibration_values_part_1():

    for key, value in part_1_inputs.items():
        res = get_calibration_value_part_1(key)
        assert res == value


def test_part1():
    res = part1(list(part_1_inputs.keys()))

    assert res == 142


part2_inputs = {
    "two1nine": 29,
    "eightwothree": 83,
    "abcone2threexyz": 13,
    "xtwone3four": 24,
    "4nineeightseven2": 42,
    "zoneight234": 14,
    "7pqrstsixteen": 76,
}


def test_calibration_values_part_2():
    for key, value in part2_inputs.items():
        res = get_calibration_value_part_2(key)
        assert res == value


def test_part_2():
    res = part2(list(part2_inputs.keys()))
    assert res == 281
