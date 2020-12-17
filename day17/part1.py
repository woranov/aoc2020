import collections

CYCLES = 6


def neighbors(x, y, z):
    for x_n in range(x - 1, x + 2):
        for y_n in range(y - 1, y + 2):
            for z_n in range(z - 1, z + 2):
                if (x, y, z) != (x_n, y_n, z_n):
                    yield x_n, y_n, z_n


def compute(data):
    """
    >>> compute([".#.", "..#", "###"])
    112
    """
    grid = {}

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                grid[(x, y, 0)] = True

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
