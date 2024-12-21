"""

"""
def main():
    fileName = "input.txt"
    with open(fileName) as file:
        data = file.readlines()
    data = [list(map(int, l.split())) for l in data]
    list1 = [l[0] for l in data]
    list2 = [l[1] for l in data]
    list1.sort()
    list2.sort()
    diff = []
    for (x, y) in zip(list1, list2):
        diff.append(abs(x - y))
    return sum(diff)

def part2():
    fileName = "input.txt"
    with open(fileName) as file:
        data = file.readlines()
    data = [list(map(int, l.split())) for l in data]
    list1 = [l[0] for l in data]
    list2 = [l[1] for l in data]
    d = {key: 0 for key in list1}
    for x in list2:
        if x not in d:
            continue
        d[x] = d.get(x, 0) + 1
    score = 0
    for (k, v) in d.items():
        score += k*v
    print(score)

if __name__ == "__main__":
    print(main())
    part2()
