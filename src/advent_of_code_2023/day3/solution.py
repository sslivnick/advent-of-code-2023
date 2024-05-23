from collections import defaultdict


def part_1(grid: list[list[str]]):
    digits = "0123456789."
    current_num = 0
    found_gears = []
    valid = False

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isdigit():
                current_num = current_num * 10 + int(grid[i][j])
                for ii in [i - 1, i, i + 1]:
                    for jj in [j - 1, j, j + 1]:
                        if out_of_bounds(grid, j, ii, jj):
                            continue
                        if grid[ii][jj] not in digits:
                            valid = True

            else:
                if valid:
                    found_gears.append(current_num)
                    valid = False
                current_num = 0

    return sum(found_gears)

def out_of_bounds(grid, j, ii, jj):
    return ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[j])

def part_2(grid: list[list[str]]):
    current_num = 0
    found_stars = defaultdict(list)
    valid = False
    star_cordinates = set()
    gear_ratio = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isdigit():
                current_num = current_num * 10 + int(grid[i][j])
                for ii in [i - 1, i, i + 1]:
                    for jj in [j - 1, j, j + 1]:
                        if out_of_bounds(grid, j, ii, jj):
                            continue
                        if grid[ii][jj] == "*":
                            valid = True
                            star_cordinates.add((ii, jj))

            else:
                if valid:
                    for star in star_cordinates:
                        found_stars[star].append(current_num)
                    valid = False
                    star_cordinates.clear()
                current_num = 0

    for _, nums in found_stars.items():
        if len(nums) == 2:
            gear_ratio += nums[0] * nums[1]
    
    return gear_ratio


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    grid = [[col for col in line] for line in lines]

    part1_res = part_1(grid)
    print(f"result for part 1 is {part1_res}")

    part2_res = part_2(grid)
    print(f"result for part 2 is {part2_res}")

