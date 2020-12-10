import collections


def compute(data):
    """
    >>> compute(["16", "10", "15", "5", "1", "11", "7", "19", "6", "12", "4"])
    35
    """
    data = sorted(map(int, data))
    inlet = 0
    outlet = data[-1] + 3

    diffs = collections.Counter(b - a for a, b in zip([inlet] + data, data + [outlet]))

    return diffs[1] * diffs[3]


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
