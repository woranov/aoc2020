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
    37
    """
    grid = [*map(list, data)]

    rows = len(grid)
    cols = len(grid[0])

    while True:
        new_grid = [row[:] for row in grid]

        for r_idx in range(rows):
            for c_idx in range(cols):
                sym = new_grid[r_idx][c_idx]

                if sym == ".":
                    continue
                else:
                    count = sum(
                        grid[nb_r][nb_c] == "#"
                        for nb_r in range(max(0, r_idx - 1), min(rows, r_idx + 2))
                        for nb_c in range(max(0, c_idx - 1), min(cols, c_idx + 2))
                        if (nb_r, nb_c) != (r_idx, c_idx)
                    )
                    if sym == "L" and count == 0:
                        new_grid[r_idx][c_idx] = "#"
                    elif sym == "#" and count >= 4:
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
