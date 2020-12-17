import collections

CYCLES = 6


def neighbors(x, y, z):
    for x_n in range(x - 1, x + 2):
        for y_n in range(y - 1, y + 2):
            for z_n in range(z - 1, z + 2):
                if (x, y, z) == (x_n, y_n, z_n):
                    pass
                else:
                    yield x_n, y_n, z_n


def compute(data):
    """
    >>> compute([".#.", "..#", "###"])
    112
    """
    grid = collections.defaultdict(bool)

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                grid[(x, y, 0)] = True

    for _ in range(CYCLES):
        grid_old = grid.copy()
        grid.clear()

        for x, y, z in {
            nb_cell
            for cell, active in grid_old.items()
            for nb_cell in neighbors(*cell)
            if active
        }:
            nb_count = sum(grid_old[nb] for nb in neighbors(x, y, z))
            if grid_old[(x, y, z)]:
                if nb_count in (2, 3):
                    grid[(x, y, z)] = True
            elif nb_count == 3:
                grid[(x, y, z)] = True

    return sum(grid.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))
        # print(compute([".#.", "..#", "###"]))


if __name__ == "__main__":
    main()
