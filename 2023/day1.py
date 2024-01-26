"""
Day 1
Part 1
"""

PART = 1
FILE_LOC = "./inputs/day1.txt"

import re

def part1(content):
    digits = []
    pattern = re.compile("[0-9]")
    for line in content:
        res = pattern.findall(line)
        digits += [int(res[0]+res[-1])]
    return sum(digits)

def part2(content):
    digits = []
    num_as_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_dict = dict(zip(num_as_word, [str(x) for x in range(10)]))
    pattern = re.compile("|".join(num_as_word)+"[0-9]")
    for line in content:
        find = pattern.findall(line)
        res = list(map(lambda x: num_dict.get(x, x), find))
        digits += [int(res[0]+res[-1])]
    return sum(digits)

if __name__ == "__main__":
    if PART not in (1, 2):
        raise ValueError("Part must be 1 or 2")
    file = open(FILE_LOC, 'r')
    if PART == 1:
        out = part1(file)
    else:
        out = part2(file)
    print(out)

