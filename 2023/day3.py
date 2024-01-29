"""
day 3

"""

def part1(content):
  raise NotImplementedError


def part2(content):
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
