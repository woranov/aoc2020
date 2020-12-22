_TESTCASE = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


def compute(data):
    """
    >>> compute(_TESTCASE)
    306
    """
    p1, _, p2 = data.partition("\n\n")
    p1 = [*map(int, p1.splitlines()[1:])]
    p2 = [*map(int, p2.splitlines()[1:])]

    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]

    won = p1 or p2

    return sum(i * c for i, c in enumerate(reversed(won), start=1))


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read()))
    # print(compute(_TESTCASE))


if __name__ == "__main__":
    main()
