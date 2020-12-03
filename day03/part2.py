import itertools

_TESTCASE = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".splitlines()


def compute(data):
    """
    >>> compute(_TESTCASE)
    336
    """
    lines = list(data)
    width, height = len(lines[0]), len(lines)
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    product = 1

    for dy, dx in slopes:
        coords = itertools.takewhile(
            lambda coord: coord[0] < height,
            map(lambda n: (n * dy, n * dx % width), itertools.count()),
        )
        product *= max(1, sum(lines[y][x] == "#" for y, x in coords))

    return product


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")
    # `splitlines` removes trailing "\n" whereas iter(file.open()) would not
    print(compute(input_path.read_text().splitlines()))


if __name__ == "__main__":
    main()
