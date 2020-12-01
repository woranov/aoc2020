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
    with open("input.txt") as f:
        print(compute(f.readlines()))


if __name__ == "__main__":
    main()
