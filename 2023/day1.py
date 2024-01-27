"""
Day 1
Part 1
Problem statement
A document consists of lines of text.
On each line, find the first digit and the last digit (in that order) to form a single two-digit number.
e.g.
abc1def2ghi3 -> 13
123456 -> 16
one2three -> 22

Part 2
Include both numbers as digits (e.g. 1, 2) and as words (one, two)
e.g.
one2three -> 13
eightwone -> 81  # This is the overlapping case.
"""

FILE_LOC = "./inputs/day1.txt"

import re

def part1(content):
    total = 0
    pattern = re.compile("[0-9]")
    for line in content:
        res = pattern.findall(line)
        total += int(res[0]+res[-1])
    return total

def part2(content):
    total = 0
    num_as_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_dict = dict(zip(num_as_word, [str(x) for x in range(1, 10)]))
    pattern = re.compile(f"(?=({'|'.join(num_as_word)+'|[0-9]'}))")
    for line in content:
        find = pattern.findall(line)
        res = list(map(lambda x: num_dict.get(x, x), find))
        total += int(res[0]+res[-1])
    return total

def main():
    part = input("Which part?")
    if part not in ('1', '2'):
        raise ValueError("Part must be 1 or 2")
    file = open(FILE_LOC, 'r')
    if part == '1':
        out = part1(file)
    else:
        out = part2(file)
    file.close()
    print(out)


if __name__ == "__main__":
    main()

