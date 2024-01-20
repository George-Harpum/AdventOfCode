"""
Day 1
Part 1
"""

PART = 1
FILE_LOC = "../inputs/day1.txt"

def part1(file_loc = FILE_LOC):
    
    def int_in_str(string: str):
        out = []
        for char in string:
            if char.isdigit():
                out.append(char)
        return out
    digits = []
    with open(file_loc) as file:
        for line in file.readlines():
            res = int_in_str(line)
            digits += [int(res[0] + res[-1])]
    return sum(digits)

def part2(file_loc = FILE_LOC):
    raise NotImplementedError


if __name__ == "__main__":
    if PART == 1:
        part1()
    elif PART == 2:
        part2()
    else:
        exit(1)

