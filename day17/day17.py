from collections import namedtuple
from itertools import product


Coord3D = namedtuple("Coordinates3Dimensional", "x, y z")
Coord4D = namedtuple("Coordinates4Dimensional", "x, y z w")


def parse_input(inp):
    return [[x == '#' for x in y.strip()] for y in inp]


def p1(inp):
    grid = {Coord3D(x, y, 0): xval for y, yval in enumerate(inp) for x, xval in enumerate(yval)}
    def change_state(grid, pos):
        count_active = sum(grid.get((pos.x+xdiff, pos.y+ydiff, pos.z+zdiff), 0) for xdiff, ydiff, zdiff in product((-1, 0 , 1), repeat=3) if any((xdiff, ydiff, zdiff)))
        return grid.get(pos, 0) and count_active in (2, 3) or not grid.get(pos, 0) and count_active == 3
    border = (-1, 9)
    for _ in range(6):
        grid = {Coord3D(x, y, z): change_state(grid, Coord3D(x, y, z)) for x, y, z in product(range(border[0], border[1]), repeat=3)}
        border = (border[0]-1, border[1]+1)
    return sum(grid.values())


def p2(inp):
    grid = {Coord4D(x, y, 0, 0): xval for y, yval in enumerate(inp) for x, xval in enumerate(yval)}
    def change_state(grid, pos):
        count_active = sum(grid.get((pos.x+xdiff, pos.y+ydiff, pos.z+zdiff, pos.w+wdiff), 0) for xdiff, ydiff, zdiff, wdiff in product((-1, 0 , 1), repeat=4) if any((xdiff, ydiff, zdiff, wdiff)))
        return grid.get(pos, 0) and count_active in (2, 3) or not grid.get(pos, 0) and count_active == 3
    border = (-1, 9)
    for _ in range(6):
        grid = {Coord4D(x, y, z, w): change_state(grid, Coord4D(x, y, z, w)) for x, y, z, w in product(range(border[0], border[1]), repeat=4)}
        border = (border[0]-1, border[1]+1)
    return sum(grid.values())


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
