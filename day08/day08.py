def parse_input(inp):
    return [(instr, int(val)) for instr, val in  [i.strip().split(" ") for i in inp]]


def run(instr):
    acc  = 0
    pos = 0
    visited = set()
    while pos not in visited and pos < len(instr):
        visited.add(pos)
        if instr[pos][0] == 'acc':
            acc += instr[pos][1]
            pos += 1
        elif instr[pos][0] == 'jmp':
            pos += instr[pos][1]
        else:
            pos += 1
    return acc, pos


def p1(inp):
    return run(inp)[0]


def p2(inp):
    for i, instr in enumerate(inp):
        if instr[0] == 'jmp':
            new_instr = inp[:i] + [('nop', instr[1])] + inp[i+1:]
        elif instr[0] == 'nop':
            new_instr = inp[:i] + [('jmp', instr[1])] + inp[i+1:]
        else:
            continue
        acc, pos = run(new_instr)
        if pos == len(inp):
            return acc


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
