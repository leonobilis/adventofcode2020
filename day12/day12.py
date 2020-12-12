from enum import IntEnum
from collections import namedtuple


class Dir(IntEnum):
    north = 0
    west = 1
    south = 2
    east = 3


Coord = namedtuple("Coordinates", "x y")
Rel = namedtuple("RelativeCoordinates", "dir val")


go = {
    Dir.north: lambda p, v: Coord(p.x, p.y+v),
    Dir.south: lambda p, v: Coord(p.x, p.y-v),
    Dir.west: lambda p, v: Coord(p.x-v, p.y),
    Dir.east: lambda p, v: Coord(p.x+v, p.y)
}


def parse_input(inp):
    return [(i[:1], int(i[1:])) for i in inp]


def p1(inp):
    current_dir = Dir.east
    pos = Coord(0,0)
    actions = {
        'N': lambda pos, dr, v: (go[Dir.north](pos, v), dr),
        'S': lambda pos, dr, v: (go[Dir.south](pos, v), dr),
        'E': lambda pos, dr, v: (go[Dir.east](pos, v), dr),
        'W': lambda pos, dr, v: (go[Dir.west](pos, v), dr),
        'L': lambda pos, dr, v: (pos, (dr + v/90)%4),
        'R': lambda pos, dr, v: (pos, (dr + (360-v)/90)%4),
        'F': lambda pos, dr, v: (go[dr](pos, v), dr)
    }
    for action, value in inp:
        pos, current_dir = actions[action](pos, current_dir, value)
    return abs(pos.x) + abs(pos.y)


def p2(inp):
    def move_waypoint_y(waypoint, direction, val):
        wy = waypoint.y.val + (val if waypoint.y.dir == direction else -val)
        dr = waypoint.y.dir if wy >= 0 else (Dir.north if waypoint.y.dir == Dir.south else Dir.south)
        return Coord(waypoint.x, Rel(dr, abs(wy)))

    def move_waypoint_x(waypoint, direction, val):
        wx = waypoint.x.val + (val if waypoint.x.dir == direction else -val)
        dr = waypoint.x.dir if wx >= 0 else (Dir.east if waypoint.x.dir == Dir.west else Dir.west)
        return Coord(Rel(dr, abs(wx)), waypoint.y)
    
    def rotate_left(waypoint, degrees):
        dir_change = degrees//90
        rot = (Rel(Dir((waypoint.x.dir + dir_change)%4), waypoint.x.val), Rel(Dir((waypoint.y.dir + dir_change)%4), waypoint.y.val))
        return Coord(rot[1], rot[0]) if dir_change%2 else Coord(rot[0], rot[1])

    def rotate_right(waypoint, degrees):
        return rotate_left(waypoint, 360-degrees)
    
    pos = Coord(0,0)
    waypoint = Coord(Rel(Dir.east, 10), Rel(Dir.north, 1))
    actions = {
        'N': lambda pos, w, v: (pos, move_waypoint_y(w, Dir.north, v)),
        'S': lambda pos, w, v: (pos, move_waypoint_y(w, Dir.south, v)),
        'E': lambda pos, w, v: (pos, move_waypoint_x(w, Dir.east, v)),
        'W': lambda pos, w, v: (pos, move_waypoint_x(w, Dir.west, v)),
        'L': lambda pos, w, v: (pos, rotate_left(w, v)),
        'R': lambda pos, w, v: (pos, rotate_right(w, v)),
        'F': lambda pos, w, v: (go[w.x.dir](go[w.y.dir](pos, w.y.val*v), w.x.val*v), w)
    }
    for action, value in inp:
        pos, waypoint = actions[action](pos, waypoint, value)
    return abs(pos.x) + abs(pos.y)

if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
