import collections

# >>> compute("2,1,3")
# 3544142
# >>> compute("1,2,3")
# 261214
# >>> compute("2,3,1")
# 6895259
# >>> compute("3,2,1")
# 18
# >>> compute("3,1,2")
# 362


def compute(data):
    """
    >>> compute("0,3,6")
    175594
    >>> compute("1,3,2")
    2578
    """
    spoken = collections.defaultdict(lambda: collections.deque(maxlen=2))

    starting = map(int, data.split(","))
    last_number = None
    i = 0

    for i, last_number in enumerate(starting, start=i + 1):
        spoken[last_number].append(i)

    for i in range(i + 1, 30000001):
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
