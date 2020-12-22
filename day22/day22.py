from functools import reduce


def parse_input(inp):
    return [[int(j) for j in i.split('\n')[1:]] for i in inp.split('\n\n')]


def score(cards):
    return reduce(lambda s, c: s + c[0] * c[1], enumerate(reversed(cards), 1), 0)


def p1(inp):
    player1, player2 = (i.copy() for i in inp)
    while player1 and player2:
        v1, v2 = player1.pop(0), player2.pop(0)
        if v1 > v2:
            player1.extend([v1, v2])
        else:
            player2.extend([v2, v1])
    return score(player1) if player1 else score(player2)


def game(player1, player2):
    prev = set()
    while player1 and player2:
        key = (tuple(player1), tuple(player2))
        if key in prev:
            player2 = []
            break
        prev.add(key)
        v1, v2 = player1.pop(0), player2.pop(0)
        if len(player1) >= v1 and len(player2) >= v2:
            check1, check2 = (len(v) for v in game(player1[:v1], player2[:v2]))
        else:
            check1, check2 = v1, v2
        if check1 > check2:
            player1.extend([v1, v2])
        else:
            player2.extend([v2, v1])
    return player1, player2


def p2(inp):
    player1, player2 = game(*inp)
    return score(player1) if player1 else score(player2)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
