import itertools

_TESTCASE = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip().splitlines()


def compute_part1(data, size=25):
    for i, num in enumerate(data[size:], size):
        prev = data[i - size : i]
        if any(num == a + b for a, b in itertools.combinations(prev, 2)):
            continue
        else:
            break
    else:
        assert False

    return num


def compute(data, size=25):
    """
    >>> compute(_TESTCASE, 5)
    62
    """
    data = [*map(int, data)]
    num = compute_part1(data, size=size)

    start, stop = 0, 2

    while stop < len(data):
        span = data[start:stop]
        span_sum = sum(span)
        if span_sum < num:
            stop += 1
        elif span_sum > num:
            start += 1
        else:
            break
    else:
        assert False

    return min(span) + max(span)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
