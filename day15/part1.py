import collections


def compute(data):
    """
    >>> compute("0,3,6")
    436
    >>> compute("1,3,2")
    1
    >>> compute("2,1,3")
    10
    >>> compute("1,2,3")
    27
    >>> compute("2,3,1")
    78
    >>> compute("3,2,1")
    438
    >>> compute("3,1,2")
    1836
    """
    spoken = collections.defaultdict(lambda: collections.deque(maxlen=2))

    starting = map(int, data.split(","))
    last_number = None
    i = 0

    for i, last_number in enumerate(starting, start=i + 1):
        spoken[last_number].append(i)

    for i in range(i + 1, 2021):
        if len(spoken[last_number]) <= 1:
            last_number = 0
        else:
            last_number = spoken[last_number][1] - spoken[last_number][0]

        spoken[last_number].append(i)

    return last_number


def main():
    print(compute("16,11,15,0,1,7"))


if __name__ == "__main__":
    main()
