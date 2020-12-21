_TESTCASE = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip().splitlines()


def compute(data):
    """
    >>> compute(_TESTCASE)
    'mxmxvkd,sqjhc,fvjkl'
    """
    ingredient_candidates = {}

    for line in data:
        ingredients, _, allergens = line.rstrip(")").partition(" (contains ")
        ingredients = set(ingredients.split())
        allergens = allergens.split(", ")

        for allergen in allergens:
            if allergen not in ingredient_candidates:
                ingredient_candidates[allergen] = ingredients
            else:
                ingredient_candidates[allergen] &= ingredients

    allergen_to_ingredient = {}

    while ingredient_candidates:
        allergen, candidates = next(
            (allergen, candidates)
            for allergen, candidates in ingredient_candidates.items()
            if len(candidates) == 1
        )

        allergen_to_ingredient[allergen] = ingredient = ingredient_candidates.pop(allergen).pop()

        for other in ingredient_candidates.values():
            other.discard(ingredient)

    return ",".join(ingredient for _, ingredient in sorted(allergen_to_ingredient.items()))


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
