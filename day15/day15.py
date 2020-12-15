def parse_input(inp):
    return [int(i) for i in inp.split(',')]


def play(inp, stop):
    spoken = {n: i+1 for i, n in enumerate(inp[:-1])}
    last = inp[-1]
    for i in range(len(inp), stop):
        number = i - spoken[last] if last in spoken else 0
        spoken[last] = i
        last = number
    return last


def p1(inp):
    return play(inp, 2020)


def p2(inp):
    return play(inp, 30000000)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
