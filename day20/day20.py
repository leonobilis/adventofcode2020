from numpy import array, rot90, array_equal, flipud, fliplr, concatenate, count_nonzero, logical_and
from itertools import permutations, product
from collections import namedtuple
from math import isqrt
from functools import reduce
from operator import mul


Tile = namedtuple("Tile", "tile right down")


def parse_input(inp):
    return {int(tile[0].split(' ')[1][:-1]): array([[x == '#' for x in y] for y in tile[1:] if y]) for tile in [i.split('\n') for i in inp.split('\n\n')]}


def get_tiles(inp):
    def get_nested_tiles(tile):
        hashes = set()
        nested_tiles = []
        for rot, t in product((0, 1, 2, -1), (tile, fliplr(tile), flipud(tile))):
            _tile = rot90(t, rot)
            _hash = str(_tile)
            if _hash not in hashes:
                hashes.add(_hash)
                nested_tiles.append(Tile(_tile, set(), set()))
        return nested_tiles
    
    tiles = {id: get_nested_tiles(tile) for id, tile in inp.items()}

    for t1, t2 in product(tiles, tiles):
        if t1 == t2:
            continue
        for tile in tiles[t1]:
            tile.right.update({(t2, i) for i, tile2 in enumerate(tiles[t2]) if array_equal(tile.tile[:,-1], tile2.tile[:,0])})
            tile.down.update({(t2, i) for i, tile2 in enumerate(tiles[t2]) if array_equal(tile.tile[-1], tile2.tile[0])})
    
    return tiles


def p1(tiles):
    return reduce(mul, [id for id, t in tiles.items() if any(not t2.right and not t2.down for t2 in t)])


def p2(tiles):
    shape = isqrt(len(tiles))
    flatten = lambda t: [item for sublist in t for item in sublist]
    count_down = lambda row: sum(bool(tiles[r[0]][r[1]].down) for r in row)

    def build_row(tile_id, row=[]):
        row = row + [tile_id]
        if len(row) == shape:
            return [row]
        return flatten([build_row((id, i), row) for id, i in tiles[tile_id[0]][tile_id[1]].right if id not in [r[0] for r in row]])

    rows = sorted([row for row in flatten([build_row((id, i)) for id in tiles for i in range(len(tiles[id]))]) if len(row) == shape], key=count_down, reverse=True)
    possible_down = [[j for j, row2 in enumerate(rows) if i != j and all(r2 in tiles[r[0]][r[1]].down for r, r2 in zip(row, row2))].pop() for i, row in enumerate(rows) if count_down(row) == shape]

    def follow(idx):
        if idx >= len(possible_down):
            return [idx]
        return [idx] + follow(possible_down[idx])
    
    def make_image(tiles):
        return concatenate([concatenate(row,1) for row in tiles], 0)

    images = [make_image([[tiles[id][k].tile[1:-1, 1:-1] for id, k in rows[j]] for j in follow(i)]) for i in range(len(rows)) if i not in possible_down]

    monster = array([[mx == '#' for mx in my] for my in ["                  # ",
                                                         "#    ##    ##    ###",
                                                         " #  #  #  #  #  #   "]])
    
    def check_monster(window):
        return array_equal(logical_and(window, monster), monster)

    def find_monsters(image):
        return sum(check_monster(image[y:y+monster.shape[0], x:x+monster.shape[1]]) for y, x in product(range(image.shape[0]-monster.shape[0]), range(image.shape[1]-monster.shape[1])))
    
    image, monster_count = sorted([(image, find_monsters(image)) for image in images], key=lambda x: x[1]).pop()
    
    return count_nonzero(image) - monster_count * count_nonzero(monster)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        tiles = get_tiles(inp)
        print(f"Part 1: {p1(tiles)}")
        print(f"Part 2: {p2(tiles)}")
