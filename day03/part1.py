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
    7
    """
    return sum(line[(idx * 3) % len(line)] == "#" for idx, line in enumerate(data))


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")
    # `splitlines` removes trailing "\n", iter(file.open()) would not
    print(compute(input_path.read_text().splitlines()))


if __name__ == "__main__":
    main()
