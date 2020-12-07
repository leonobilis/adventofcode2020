import re


def parse_input(inp):
    regexp1 = re.compile(r"(\w+ \w+) bags contain")
    regexp2 = re.compile(r"(\d+) (\w+ \w+) bag")
    return {regexp1.search(i).group(1): regexp2.findall(i) for i in inp}


def p1(inp):
    valid = {k for k, v in inp.items() if "shiny gold" in [i[1] for i in v]}
    valid_len = 0
    while valid_len != len(valid):
        valid_len = len(valid)
        valid.update(k for k, v in inp.items() if k not in valid and valid.intersection(i[1] for i in v))
    return len(valid)


def p2(inp):
    def bag_count(bag, bags):
        return 1 + (sum(bag_count(b[1], bags) * int(b[0]) for b in bags[bag]) if bags[bag] else 0)
    return bag_count("shiny gold", inp) - 1


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
