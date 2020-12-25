import itertools


def transform(subject, value=1):
    for loop in itertools.count(1):
        value = (subject * value) % 20201227
        yield loop, value


def compute(data):
    """
    >>> compute(["5764801", "17807724"])
    14897079
    """
    card_pk, door_pk = map(int, data)
    card_loop_size = next(loop for loop, value in transform(7) if value == card_pk)
    return next(value for loop, value in transform(door_pk) if loop == card_loop_size)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))
    # print(compute(["5764801", "17807724"]))


if __name__ == "__main__":
    main()
