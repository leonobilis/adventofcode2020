from itertools import dropwhile


def parse_input(inp):
    return [int(i) for i in inp[0]]


def mix_cups(cups, cup, repeat):
    for _ in range(repeat):
        pickup = [cups[cup]]
        pickup.append(cups[pickup[-1]])
        pickup.append(cups[pickup[-1]])
        destination = next(dropwhile(lambda x: x in pickup, ((len(cups) - 2 + x) % (len(cups)) + 1 for x in (cup, cup-1,cup-2, cup-3))))
        next_destination = cups[destination]
        cups[cup] = cups[pickup[-1]]
        cups[destination] = pickup[0]
        cups[pickup[-1]] = next_destination
        cup = cups[cup]


def p1(inp):
    cups = {c: inp[i+1] if i < len(inp) - 1 else inp[0] for i, c in enumerate(inp)}
    mix_cups(cups, inp[0], 100)
    def order(cup):
        return str(cup) + order(cups[cup]) if cup != 1 else ''
    return order(cups[1])


def p2(inp):
    cups = {**{c: inp[i+1] if i < len(inp) - 1 else len(inp)+1 for i, c in enumerate(inp)}, **{i: i+1 for i in range(len(inp)+1, 10**6)}, 10**6: inp[0]}
    mix_cups(cups, inp[0], 10**7)
    return cups[1] * cups[cups[1]]


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
