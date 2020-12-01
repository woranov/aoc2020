def compute(data):
    """
    >>> compute(None)
    """
    pass


def main():
    with open("input.txt") as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
