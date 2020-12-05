CODE_TRANS = str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})


def compute(data):
    """
    # BBFFBBFRRL (-> 822) missing
    >>> compute(["BBFFBBFRLL", "BBFFBBFRLR", "BBFFBBFRRR"])
    822
    """
    seat_ids = sorted(int(code.translate(CODE_TRANS), 2) for code in data)

    for before_id, after_id in zip(seat_ids, seat_ids[1:]):
        if before_id == after_id - 2:
            return before_id + 1


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
