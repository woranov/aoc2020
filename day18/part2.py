import functools
import re

_TESTCASE = """\
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
""".strip().splitlines()


PARENS = re.compile(r"\(([^()]+)\)")
PLUS = re.compile(r"(\d+)\+(\d+)")


def evaluate(expr):
    expr = expr.replace(" ", "")

    def evaluate_paren_match(match):
        return str(evaluate(match.group(1)))

    def evaluate_plus_match(match):
        return str(int(match.group(1)) + int(match.group(2)))

    while "(" in expr:
        expr = PARENS.sub(evaluate_paren_match, expr)

    while "+" in expr:
        expr = PLUS.sub(evaluate_plus_match, expr)

    return functools.reduce(lambda a, b: int(a) * int(b), expr.split("*"), 1)


def compute(data):
    """
    >>> compute(_TESTCASE)
    693891
    """
    return sum(map(evaluate, data))


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
