_TESTCASE = """\
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
""".strip().splitlines()


def evaluate(expr):
    idx = 0
    acc = 0
    op = None

    while idx < len(expr):
        c = expr[idx]

        if c == "(":
            group = c
            while group.count("(") > group.count(")"):
                idx += 1
                group += expr[idx]
            c = evaluate(group[1:-1])
        elif c.isdigit():
            c = int(c)

        if isinstance(c, int):
            if op is None:
                acc = c
            elif op == "*":
                acc *= c
            elif op == "+":
                acc += c
        elif c in "+*":
            op = c
        else:
            raise NotImplementedError(c)

        idx += 1

    return acc


def compute(data):
    """
    >>> compute(_TESTCASE)
    26335
    """
    return sum(evaluate(expr.replace(" ", "")) for expr in data)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
