def parse_input(inp):
    return [(set(ingredients.split(' ')), set(allergens[:-1].split(', '))) for ingredients, allergens  in [i.strip().split(' (contains ') for i in inp]]


def get_allergens_ingredients(inp):
    allergens = {a: sum(a in i2[1] for i2 in inp) for a in {j for i in inp for j in i[1]}}
    ingredients = {name: [i2[1] for i2 in inp if name in i2[0]] for name in {j for i in inp for j in i[0]}}
    allergens_free = {name: len(allergens_lists) for name, allergens_lists in ingredients.items() if not {a for a in allergens if not sum(a in al for al in allergens_lists) - allergens[a]}}
    return allergens, ingredients, allergens_free


def p1(inp):
    _, _, allergens_free = get_allergens_ingredients(inp)
    return sum(allergens_free.values())


def p2(inp):
    allergens, ingredients, allergens_free = get_allergens_ingredients(inp)
    ingredients = sorted([(name, {a for a in allergens if not sum(a in al for al in allergens_lists) - allergens[a]}) for name, allergens_lists in ingredients.items() if name not in allergens_free], key=lambda x: len(x[1]), reverse=True)
    ingredients_wit_alergen = {}
    known_alergens = set()
    for _ in range(len(ingredients)):
        ingedient, alergen = ingredients.pop()
        ingredients_wit_alergen[ingedient] = (alergen - known_alergens).pop()
        known_alergens.add(ingredients_wit_alergen[ingedient])
        ingredients.sort(key=lambda x: len(x[1] - known_alergens), reverse=True)
    return ','.join(i[0] for i in sorted(ingredients_wit_alergen.items(), key=lambda x: x[1]))


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = parse_input(f.readlines())
        print(f"Part 1: {p1(inp)}")
        print(f"Part 2: {p2(inp)}")
