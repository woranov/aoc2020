import functools

_TESTCASE = """\
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip().split(
    "\n\n"
)


def compute(data):
    """
    >>> compute(_TESTCASE)
    6
    """
    return sum(
        len(
            functools.reduce(
                set.__and__,
                map(set, group.splitlines()),
            )
        )
        for group in data
    )


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().split("\n\n")))


if __name__ == "__main__":
    main()
