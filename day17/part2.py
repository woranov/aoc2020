import collections
import itertools

CYCLES = 6
DIMENSIONS = 4


def neighbors(*coord):
    for nb_c in itertools.product(*(range(c - 1, c + 2) for c in coord)):
        if coord != nb_c:
            yield nb_c


def compute(data):
    """
    >>> compute([".#.", "..#", "###"])
    848
    """
    grid = {}

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                grid[(x, y) + (0,) * (DIMENSIONS - 2)] = True

    for _ in range(CYCLES):
        grid_old = grid.copy()
        grid.clear()

        neighbor_counter = collections.Counter(
            nb_coord for coord in grid_old for nb_coord in neighbors(*coord)
        )

        for coord, nb_count in neighbor_counter.items():
            if coord in grid_old:
                if nb_count in (2, 3):
                    grid[coord] = True
            elif nb_count == 3:
                grid[coord] = True

    return sum(grid.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
