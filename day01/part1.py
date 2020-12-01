def compute(data):
    """
    >>> compute(("1721", "979", "366", "299", "675", "1456"))
    514579
    """
    nums = {*map(int, data)}
    for num1 in nums:
        if (num2 := 2020 - num1) in nums:
            break
    else:
        assert False

    return num1 * num2


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f))


if __name__ == "__main__":
    main()
