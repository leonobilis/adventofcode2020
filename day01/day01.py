from itertools import combinations


def get_entries(input, number):
    return [entries for entries in combinations(input, number) if sum(entries) == 2020][0]


def p1(input):
    a, b = get_entries(input, 2)
    return a*b


def p2(input):
    a, b, c = get_entries(input, 3)
    return a*b*c


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = [int(i) for i in f.readlines()]
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
