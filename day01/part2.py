def find_pair(nums, remaining):
    for num1 in nums:
        num2 = remaining - num1
        if num2 in nums:
            return num1, num2
    else:
        return None, None


def compute(data):
    """
    >>> compute(("1721", "979", "366", "299", "675", "1456"))
    241861950
    """

    nums = {*map(int, data)}

    for num1 in nums:
        num2, num3 = find_pair(nums, remaining=2020 - num1)
        if num2 and num3:
            break
    else:
        assert False

    return num1 * num2 * num3


def main():
    with open("input.txt") as f:
        print(compute(f.readlines()))


if __name__ == "__main__":
    main()
