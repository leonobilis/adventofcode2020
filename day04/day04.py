def parse_input(inp):
    return [dict(j.split(":") for j in i.replace("\n", " ").split(" ")) for i in inp.split("\n\n")]


def p1(passports):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return sum(all(field in passport for field in required_fields) for passport in passports)



def p2(passports):
    required_fields = {
        "byr": lambda f: len(f) == 4 and 1920 <= int(f) <= 2002,
        "iyr": lambda f: len(f) == 4 and 2010 <= int(f) <= 2020,
        "eyr": lambda f: len(f) == 4 and 2020 <= int(f) <= 2030,
        "hgt": lambda f: len(f) > 3 and (150 <= int(f[:-2]) <= 193 if f.endswith("cm") else 59 <= int(f[:-2]) <= 79),
        "hcl": lambda f: len(f) == 7 and f[0] == '#' and f[1:].isalnum(),
        "ecl": lambda f: len(f) == 3 and f in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda f: len(f) == 9 and f.isdigit()
    }
    return sum(all(validate(passport.get(field, "")) for field, validate in required_fields.items()) for passport in passports)


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
