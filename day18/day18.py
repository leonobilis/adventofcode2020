import operator
from itertools import takewhile


def parse_input(inp):
    return [i.strip().replace('(', '( ').replace(')', ' )').split(' ') for i in inp]


def convert(expression, add_first=False):
    output = []
    stack = []
    for e in expression:
        if e.isdigit():
            output.append(int(e))
        elif e == '*':
            if stack and stack[-1] != '(':
               output.append(stack.pop())
            stack.append(e)
        elif e == '+':
            if stack and (stack[-1] == '+' if add_first else stack[-1] != '('):
               output.append(stack.pop())
            stack.append(e)
        elif e == '(':
            stack.append(e)
        elif e == ')':
            to_out = list(takewhile(lambda x: x != '(', reversed(stack)))
            output.extend(to_out)
            stack = stack[:-len(to_out)-1]
    output += reversed(stack)
    return output


def calc(tokens):
    result = []
    oper = {'+': operator.add, '*': operator.mul}
    for t in tokens:
        result.append(oper[t](result.pop(), result.pop()) if t in oper else int(t))
    return result.pop()


def p1(inp):
    return sum(calc(convert(i)) for i in inp)


def p2(inp):
    return sum(calc(convert(i, add_first=True)) for i in inp)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
