import collections
import functools

_TESTCASE = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip().splitlines()


def compute(data):
    """
    >>> compute(_TESTCASE)
    5
    """
    ingredient_candidates = {}
    ingredient_counter = collections.Counter()

    for line in data:
        ingredients, _, allergens = line.rstrip(")").partition(" (contains ")
        ingredients = set(ingredients.split())
        allergens = allergens.split(", ")

        ingredient_counter.update(ingredients)

        for allergen in allergens:
            if allergen not in ingredient_candidates:
                ingredient_candidates[allergen] = ingredients
            else:
                ingredient_candidates[allergen] &= ingredients

    # noinspection PyTypeChecker
    all_candidates = functools.reduce(set.union, ingredient_candidates.values())

    no_allergen_ingredients = set(ingredient_counter) - all_candidates

    return sum(ingredient_counter[ingredient] for ingredient in no_allergen_ingredients)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
