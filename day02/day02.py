import re


def parse_input(inp):
    regexp = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    return [(int(s.group(1)), int(s.group(2)), s.group(3), s.group(4)) for s in [regexp.search(i) for i in inp]]


def p1(passwords):
    return sum(num_min <= password.count(letter) <= num_max for num_min, num_max, letter, password in passwords)


def p2(passwords):
    return sum((password[num_min-1] == letter) ^ (password[num_max-1] == letter) for num_min, num_max, letter, password in passwords)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
