def parse_input(inp):
    l = [int(i) for i in inp]
    return sorted(l + [0, max(l) + 3])


def p1(inp):
    diff = [inp[i+1] - inp[i] for i in range(len(inp) - 1)]
    return  sum(d==1 for d in diff) * sum(d==3 for d in diff)


def p2(inp):
    known = {inp[-1]: 1}
    possibilities = {inp[i]: [inp[i+j] for j in range(1,4) if i+j < len(inp) and inp[i+j] - inp[i] <=3] for i in range(len(inp) - 1)}
    def coun_pos(adapter):
        val = known.get(adapter, None) or sum(coun_pos(a) for a in possibilities[adapter])
        known[adapter] = val
        return val
    return coun_pos(0)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
