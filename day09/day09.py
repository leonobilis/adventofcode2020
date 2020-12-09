from itertools import combinations


def parse_input(inp):
    return [int(i.strip()) for i in inp]


def p1(inp):
    return next(number for i, number in enumerate(inp) if i >= 25 and not next(filter(lambda x: x[0] + x[1] == number, combinations(inp[i-25:i], 2)), False))


def p2(inp):
    invalid_number = p1(inp)
    def calc(pos, numbers):
        return numbers if sum(numbers) == invalid_number else (set() if sum(numbers) > invalid_number or pos > len(inp) else calc(pos+1, numbers | {inp[pos+1]}))
    numbers = next(filter(bool, (calc(i, {num}) for i, num in enumerate(inp))))
    return max(numbers) + min(numbers)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
