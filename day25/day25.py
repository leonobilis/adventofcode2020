def parse_input(inp):
    return int(inp[0]), int(inp[1])


def find_loop_size(value):
    a = 7
    i = 0
    while a != value:
        i += 1
        a = transform(a)
    return i


def transform(value, subject=7, repeat=1):
    for _ in range(repeat):
        value = (value*subject) % 20201227
    return value


def p1(inp):
    card_pub, door_pub = inp
    return transform(card_pub, subject=card_pub, repeat=find_loop_size(door_pub))


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
