import re
from functools import reduce
from operator import mul


def parse_input(inp):
    rules, your_ticket, nearby_tickets = inp.split("\n\n")
    regexp = re.compile(r"([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)")
    return {k: lambda x, v=v: v[0] <= x <= v[1] or v[2] <= x <= v[3] for k, v in [(r2.group(1), (int(r2.group(2)), int(r2.group(3)), int(r2.group(4)), int(r2.group(5)))) for r2 in [regexp.search(r) for r in rules.split('\n')]]}, \
        [int(y) for y in your_ticket.split('\n')[1].split(',')], [[int(n2) for n2 in n.split(',')] for n in nearby_tickets.split('\n')[1:]]


def validate(rules, tickets):
    return [(t, [t2 for t2 in t if not any(r(t2) for r in rules.values())]) for t in tickets]


def p1(inp):
    rules, _, nearby_tickets = inp
    return sum(sum(errors) for _, errors in validate(rules, nearby_tickets))


def p2(inp):
    rules, your_ticket, nearby_tickets = inp
    tickets = [n for n, errors in validate(rules, nearby_tickets) if not errors] + [your_ticket]
    found = {}
    for _ in range(len(rules)):
        field = min([(name, set.intersection(*[{i for i, field in enumerate(ticket) if i not in found.values() and rule(field)} for ticket in tickets])) for name, rule in rules.items() if name not in found], key=lambda x: len(x[1]))
        found[field[0]] = field[1].pop()
    return reduce(mul, [your_ticket[i] for name, i in found.items() if name.startswith('departure')])


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
