from functools import reduce
from operator import mul


def parse_input(inp):
    return [[1 if j=='#' else 0 for j in i.strip()] for i in inp]


def count_trees(grid, right, down):
    return sum(grid[i][(i*right//down)%len(grid[0])] for i in range(0, len(grid), down))


def p1(grid):
    return count_trees(grid, right=3, down=1)


def p2(grid):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    return reduce(mul, [count_trees(grid, right=s[0], down=s[1]) for s in slopes])


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
