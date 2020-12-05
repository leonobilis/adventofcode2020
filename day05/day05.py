def parse_input(inp):
    return [(i[:7], i[7:10]) for i in inp]


def get_pos(boarding_pass):
    row = (0, 127)
    for r in boarding_pass[0]:
        diff = (row[1] - row[0])//2 + 1
        row = (row[0] + diff if r == 'B' else row[0], row[1] - diff if r == 'F' else row[1])
    col = (0, 7)
    for c in boarding_pass[1]:
        diff = (col[1] - col[0])//2 + 1
        col = (col[0] + diff if c == 'R' else col[0], col[1] - diff if c == 'L' else col[1])
    return row[0], col[0]


def p1(inp):
    return max(row*8 + column for row, column in [get_pos(i) for i in inp])   


def p2(inp):
    occupied_seats = {row*8 + column for row, column in [get_pos(i) for i in inp]}
    all_seats = {i for i in range(128*8)}
    return next(filter(lambda x: x-1 in occupied_seats and x+1 in occupied_seats, all_seats - occupied_seats))


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
