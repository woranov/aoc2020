def compute(data):
    """
    >>> compute(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])
    1
    """

    cnt = 0
    for idxs, (char, _), password in map(str.split, data):
        idx1, idx2 = map(int, idxs.split("-"))
        cnt += (password[idx1 - 1] == char) ^ (password[idx2 - 1] == char)

    return cnt


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f))


if __name__ == "__main__":
    main()
