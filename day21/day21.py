def parse_input(inp):
    return [(set(ingredients.split(' ')), set(allergens[:-1].split(', '))) for ingredients, allergens  in [i.strip().split(' (contains ') for i in inp]]

def p1(inp):
    allergens = {a: set.intersection(*[i2[0] for i2 in inp if a in i2[1]]) for a in {j for i in inp for j in i[1]}}
    ingredients = {j for i in inp for j in i[0]}
    return sum(sum(ig in i[0] for i in inp) for ig in ingredients.difference(*allergens.values()))


def p2(inp):
    allergens = sorted([(a, set.intersection(*[i2[0] for i2 in inp if a in i2[1]])) for a in {j for i in inp for j in i[1]}], key=lambda x: len(x[1]), reverse=True)
    known_ingredients = {}
    for _ in range(len(allergens)):
        alergen, ingedient = allergens.pop()
        known_ingredients[ingedient.pop()] = alergen
        allergens = sorted([(a, ingedients.difference(known_ingredients.keys())) for a, ingedients in allergens], key=lambda x: len(x[1]), reverse=True)
    return ','.join(i[0] for i in sorted(known_ingredients.items(), key=lambda x: x[1]))


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
