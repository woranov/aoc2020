CODE_TRANS = str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})


def compute(data):
    """
    >>> compute(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"])
    820
    """
    return max(int(code.translate(CODE_TRANS), 2) for code in data)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
