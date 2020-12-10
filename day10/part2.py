import functools
import itertools
import math


@functools.lru_cache()
def num_choices(chainsize, max_diff):
    """
    >>> num_choices(3, max_diff=3) == math.comb(3, 3) + math.comb(3, 2) + math.comb(3, 1)  # noqa: E501
    True
    """
    ks = (chainsize - i for i in range(min(chainsize + 1, max_diff)))

    return sum(math.comb(chainsize, k) for k in ks)


def compute(data):
    """
    >>> compute(["16", "10", "15", "5", "1", "11", "7", "19", "6", "12", "4"])
    8
    """
    max_diff = 3

    data = sorted(map(int, data))
    inlet = 0
    outlet = max_diff

    arrangements = 1

    diff_groups = itertools.groupby(
        b - a for a, b in zip([inlet] + data, data + [outlet])
    )

    for diff, chain in diff_groups:
        if diff == max_diff:
            continue

        # -1 for the choice of not skipping any number
        size = len(list(chain)) - 1
        if size < 1:
            continue

        arrangements *= num_choices(size, max_diff=max_diff)

    return arrangements


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
