from itertools import product, dropwhile
from copy import deepcopy
from collections import namedtuple


Coord = namedtuple("Coordinates", "x, y")


def parse_input(inp):
    return [list((len(inp[0])+2) * 'X')] + [list('X' + i.strip() + 'X') for i in inp] + [list((len(inp[0])+2) * 'X')]


def shift(grid, adjacent, tolerance):
    prev = [None,[None,None]]
    while any(grid[y][x] != prev[y][x] for y, x in product(range(1, len(grid) - 1), range(1, len(grid[0]) - 1))):
        prev = deepcopy(grid)
        for y, x in product(range(1, len(grid) - 1), range(1, len(grid[0]) - 1)):
            if grid[y][x] == 'L' and not any(a == '#' for a in adjacent(prev, Coord(x, y))):
                grid[y][x] = '#'
            elif grid[y][x] == '#' and sum(a == '#' for a in adjacent(prev, Coord(x, y))) >= tolerance:
                grid[y][x] = 'L'
    return grid


def p1(inp):
    def adjacent(grid, pos):
        return grid[pos.y-1][pos.x-1:pos.x+2] + [grid[pos.y][pos.x-1], grid[pos.y][pos.x+1]] + grid[pos.y+1][pos.x-1:pos.x+2]
    return sum(j == '#' for i in shift(deepcopy(inp), adjacent, 4) for j in i)


def p2(inp):
    def adjacent(grid, pos):
        return [
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), grid[pos.y][pos.x+1:])),
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), reversed(grid[pos.y][:pos.x]))),
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), (g[pos.x] for g in grid[pos.y+1:]))),
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), (g[pos.x] for g in reversed(grid[:pos.y])))),
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), (grid[y][x] for y, x in zip(range(pos.y+1, len(grid)), range(pos.x+1, len(grid[0])))))),
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), (grid[y][x] for y, x in zip(range(pos.y-1, -1, -1), range(pos.x+1, len(grid[0])))))),
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), (grid[y][x] for y, x in zip(range(pos.y-1, -1, -1), range(pos.x-1, -1, -1))))),
            next(dropwhile(lambda g: g not in ('L', '#', 'X'), (grid[y][x] for y, x in zip(range(pos.y+1, len(grid)), range(pos.x-1, -1, -1)))))
        ]
    return sum(j == '#' for i in shift(deepcopy(inp), adjacent, 5) for j in i)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
