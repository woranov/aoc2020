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
    grid = collections.defaultdict(bool)

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#":
                grid[(x, y) + (0,) * (DIMENSIONS - 2)] = True

    for _ in range(CYCLES):
        grid_old = grid.copy()
        grid.clear()

        for nb_coord in {
            nb_coord
            for coord, active in grid_old.items()
            for nb_coord in neighbors(*coord)
            if active
        }:
            nb_count = sum(grid_old[nb] for nb in neighbors(*nb_coord))
            if grid_old[nb_coord]:
                if nb_count in (2, 3):
                    grid[nb_coord] = True
            elif nb_count == 3:
                grid[nb_coord] = True

    return sum(grid.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
