import re
from itertools import product


def parse_input(inp):
    mask_regexp = re.compile(r"(mask) = ([01X]+)")
    mem_regexp = re.compile(r"(mem)\[(\d+)\] = (\d+)")
    return [mask_regexp.findall(i)[0] if mask_regexp.match(i) else mem_regexp.findall(i)[0] for i in inp]


def p1(inp):
    mask = 0
    mem = {}
    for i in inp:
        if i[0] == 'mask':
            mask = (int(i[1].replace('X', '1'), 2), int(i[1].replace('X', '0'), 2))
        else:
            mem[int(i[1])] = int(i[2]) & mask[0] | mask[1]
    return sum(mem.values())


def p2(inp):
    masks = []
    mem = {}
    for i in inp:
        if i[0] == 'mask':
            masks = [int(i[1].replace('X', '0'), 2)]
            for p in product('01', repeat=i[1].count('X')):
                mask = i[1].replace('1', 'Y').replace('0', 'Y')
                for p2 in p:
                    mask = mask.replace('X', p2, 1)
                masks.append((int(mask.replace('Y', '1'), 2), int(mask.replace('Y', '0'), 2)))
        else:
            addr = int(i[1]) | masks[0]
            for mask in masks[1:]:
                mem[addr & mask[0] | mask[1]] = int(i[2])
    return sum(mem.values())


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
