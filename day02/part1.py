def compute(data):
    """
    >>> compute(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])
    2
    """

    cnt = 0
    for cnt_range, (char, _), password in map(str.split, data):
        lo, hi = map(int, cnt_range.split("-"))
        cnt += lo <= password.count(char) <= hi

    return cnt


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f))


if __name__ == "__main__":
    main()
