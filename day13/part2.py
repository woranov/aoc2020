import itertools


def compute(data):
    """
    >>> compute([None, "7,13,x,x,59,x,31,19"])
    1068781
    >>> compute([None, "17,x,13,19"])
    3417
    >>> compute([None, "67,7,59,61"])
    754018
    >>> compute([None, "67,x,7,59,61"])
    779210
    >>> compute([None, "67,7,x,59,61"])
    1261476
    >>> compute([None, "1789,37,47,1889"])
    1202161486
    """
    buses = [(int(b), i) for i, b in enumerate(data[1].split(",")) if b != "x"]

    base = 0
    factor = int(buses[0][0])

    for bus, offset in buses[1:]:
        base += next(
            filter(
                lambda x: (x + base + offset) % bus == 0,
                (factor * n for n in itertools.count(1)),
            )
        )
        factor *= bus

    return base


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
