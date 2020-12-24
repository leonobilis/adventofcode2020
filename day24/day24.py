from collections import namedtuple, defaultdict


Tile = namedtuple("Tile", "x y")


def parse_input(inp):
    inp = [Tile(x=4*(i.count('e')-i.count('w')) + 2*(i.count('nw')+i.count('sw')-i.count('ne')-i.count('se')),
                y=3*(i.count('nw')-i.count('se') + i.count('ne')-i.count('sw'))) for i in inp]
    return defaultdict(int, {i: inp.count(i) % 2 for i in inp})


def p1(tiles):
    return sum(tiles.values())


def adjacent(tile, tiles):
    return sum(tiles[Tile(tile.x+xdiff, tile.y+ydiff)] for xdiff, ydiff in ((4,0), (-4,0), (2,3), (2,-3), (-2,3), (-2,-3)))


def flip(tiles, repeat=100):
    for _ in range(repeat):
        new_tiles = defaultdict(int)
        for tile, value in tiles.copy().items():
            new_tiles[tile] = int(0 < adjacent(tile, tiles) <= 2) if value else int(adjacent(tile, tiles) == 2)
        tiles.update(new_tiles)
    return tiles


def p2(tiles):
    [adjacent(t, tiles) for t in tiles.copy()]
    tiles = flip(tiles)
    return sum(tiles.values())


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
