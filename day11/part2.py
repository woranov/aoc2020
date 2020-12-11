import functools
import itertools

_TESTCASE = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip().splitlines()


def compute(data):
    """
    >>> compute(_TESTCASE)
    26
    """
    grid = [*map(list, data)]

    rows = len(grid)
    cols = len(grid[0])

    # doing some memoization but its pretty pointless

    @functools.lru_cache(maxsize=None)
    def get_directions(r, c):
        return {
            "↓": tuple(zip(itertools.repeat(r), range(c + 1, cols))),
            "↑": tuple(zip(itertools.repeat(r), range(c - 1, -1, -1))),
            "→": tuple(zip(range(r + 1, rows), itertools.repeat(c))),
            "←": tuple(zip(range(r - 1, -1, -1), itertools.repeat(c))),
            "↗": tuple(zip(range(r + 1, rows), range(c + 1, cols))),
            "↖": tuple(zip(range(r + 1, rows), range(c - 1, -1, -1))),
            "↙": tuple(zip(range(r - 1, -1, -1), range(c + 1, cols))),
            "↘": tuple(zip(range(r - 1, -1, -1), range(c - 1, -1, -1))),
        }

    non_floor_seats = [
        (r, c) for r in range(rows) for c in range(cols) if grid[r][c] != "."
    ]

    while True:
        new_grid = [row[:] for row in grid]

        for r_idx, c_idx in non_floor_seats:
            sym = new_grid[r_idx][c_idx]

            if sym == ".":
                continue
            else:
                count = 0
                for direction in get_directions(r_idx, c_idx).values():
                    for nb_r, nb_c in direction:
                        if grid[nb_r][nb_c] == ".":
                            continue
                        elif grid[nb_r][nb_c] == "#":
                            count += 1
                        break

                if sym == "L" and count == 0:
                    new_grid[r_idx][c_idx] = "#"
                elif sym == "#" and count >= 5:
                    new_grid[r_idx][c_idx] = "L"

        if new_grid == grid:
            break
        else:
            grid = new_grid

    return sum(seat == "#" for row in grid for seat in row)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
