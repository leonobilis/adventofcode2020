import re

def parse_input(inp):
    rules, messages = inp.split('\n\n')
    rules = dict(rule.split(': ') for rule in rules.split('\n'))
    return rules, messages.split('\n')

def get_regex(rules):
    translate = {'"a"': 'a', '"b"':'b', '|':'|'}
    rules.update(translate)
    def replace(value, limit=12):
        result = translate.get(value) or ('' if not limit else '(' + ''.join(replace(rules[v], limit-1) for v in value.split(' ')) + ')')
        translate[value] = result
        return result
    return '^' + replace('0') + '$'


def p1(inp):
    rules, messages = inp
    r = re.compile(get_regex(rules))
    return sum(bool(r.match(m)) for m in messages)


def p2(inp):
    rules, messages = inp
    r = re.compile(get_regex({**rules, '8': '42 | 42 8', '11': '42 31 | 42 11 31'}))
    return sum(bool(r.match(m)) for m in messages)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
