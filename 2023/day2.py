"""
Day2
Problem statement

A bag contains red, blue, and green cubes. 
A game consists of several random selections of cubes are taken from the bag (with replacement)
Each game has a new bag with variable number of cubes.

Part 1
Which games are possible provided a bag contains exactly 12 red, 13 green, and 14 blue cubes?

Part 2
What are the minimum number of each colour cube for the game to be possible
Multiply those numbers together and sum that result for each game
e.g. a game requiring 2 red, 3 blue, and 4 green has a 'power' of 24. 
"""

FILE_LOC = ".\inputs\day2.txt"


def test_max(string, red_max, green_max, blue_max):
    split = string.split(' ')
    num = int(split[0])
    match split[1].strip('\n'):
        case 'blue':
            if num > blue_max:
                return False
        case 'red':
            if num > red_max:
                return False
        case 'green':
            if num > green_max:
                return False
    return True

def part1(content, rMax=12, gMax=13, bMax=14):
    total = 0
    for line in content:
        game_parts = line.split(': ')
        game_id = int(game_parts[0][5:])
        selections = game_parts[1].split('; ')
        tag = True
        for s in selections:
            colours = s.split(', ')
            if all([test_max(c, rMax, gMax, bMax) for c in colours]) is False:
                tag = False
                break
        if tag is True:
            total += game_id
    return total


def part2():
    raise NotImplementedError


def main():
    part = input("Which part?")
    try:
        with open(FILE_LOC, 'r') as file:
            match part:
                case '1':
                    out = part1(file)
                case '2':
                    out = part2(file)
                case _:
                    raise ValueError("Value must be 1 or 2")
            print(out) 
    except FileNotFoundError:
        print("The file doesn't exist")
        exit(1)

if __name__ == "__main__":
    main()

