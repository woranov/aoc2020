import functools

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


@functools.lru_cache(maxsize=None)
def combat(p1, p2):
    history = set()

    while p1 and p2:
        state = p1, p2
        if state in history:
            return True, p1
        else:
            history.add(state)

        c1, p1 = p1[0], p1[1:]
        c2, p2 = p2[0], p2[1:]

        if len(p1) >= c1 and len(p2) >= c2:
            p1_won, _ = combat(p1[:c1], p2[:c2])
        else:
            p1_won = c1 > c2

        if p1_won:
            p1 += (c1, c2)
        else:
            p2 += (c2, c1)

    return bool(p1), p1 or p2


def compute(data):
    """
    >>> compute(_TESTCASE)
    291
    """
    p1, _, p2 = data.partition("\n\n")
    p1 = tuple(map(int, p1.splitlines()[1:]))
    p2 = tuple(map(int, p2.splitlines()[1:]))

    _, won = combat(p1, p2)
    return sum(i * c for i, c in enumerate(reversed(won), start=1))


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read()))
    # print(compute(_TESTCASE))


if __name__ == "__main__":
    main()
