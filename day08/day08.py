from collections import namedtuple


Computer = namedtuple("Computer", "counter acc")
Instruction = namedtuple("Instruction", "oper arg")


def parse_input(inp):
    return [Instruction(instr, int(val)) for instr, val in  [i.strip().split(" ") for i in inp]]


def run(program):
    operations = {
        'acc': lambda c, x: Computer(counter=c.counter + 1, acc=c.acc + x),
        'jmp': lambda c, x: Computer(counter=c.counter + x, acc=c.acc),
        'nop': lambda c, x: Computer(counter=c.counter + 1, acc=c.acc),
    }
    computer = Computer(0, 0)
    visited = set()
    while computer.counter not in visited and computer.counter < len(program):
        visited.add(computer.counter)
        instr = program[computer.counter]
        computer = operations[instr.oper](computer, instr.arg)
    return computer


def p1(inp):
    return run(inp).acc


def p2(inp):
    swap = lambda i, prog: prog[:i] + [Instruction('nop' if prog[i].oper == 'jmp' else 'jmp', prog[i].arg)] + prog[i+1:]
    return next(filter(lambda c: c.counter == len(inp), [run(swap(i, inp)) for i, instr in enumerate(inp) if instr.oper != 'acc'])).acc


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
