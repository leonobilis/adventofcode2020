from math import ceil
from sympy.ntheory.modular import crt


def parse_input(inp):
    return int(inp[0]), [(int(bus), i) for i, bus in enumerate(inp[1].strip().split(',')) if bus != 'x']


def p1(inp):
    earliest_timestamp, bus_ids = inp
    bus = min(((bus_id, ceil(earliest_timestamp/bus_id) * bus_id) for bus_id, _ in bus_ids), key=lambda x: x[1])
    return bus[0] * (bus[1] - earliest_timestamp)


def p2(inp):
    _, bus_ids = inp
    return crt([bus_id for bus_id, _ in bus_ids], [-time for _, time in bus_ids])[0]


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
