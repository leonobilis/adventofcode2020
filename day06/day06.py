def parse_input(inp):
    return [[set(j) for j in i.split("\n")] for i in inp.split("\n\n")]


def p1(inp):
    return sum(len(set.union(*i)) for i in inp)


def p2(inp):
    return sum(len(set.intersection(*i)) for i in inp)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
