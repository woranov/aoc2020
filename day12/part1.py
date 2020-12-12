DIRECTIONS = "NESW"


def shift_direction(current, rotation=1):
    new_idx = (DIRECTIONS.index(current) + rotation) % len(DIRECTIONS)
    return DIRECTIONS[new_idx]


def compute(data):
    """
    >>> compute(["F10", "N3", "F7", "R90", "F11"])
    25
    """
    n, e = 0, 0
    facing = "E"

    for instruction in data:
        action = instruction[0]
        value = int(instruction[1:])

        if action == "F":
            action = facing

        if action == "L":
            facing = shift_direction(facing, -value // 90)
        elif action == "R":
            facing = shift_direction(facing, value // 90)
        elif action == "N":
            n += value
        elif action == "E":
            e += value
        elif action == "S":
            n -= value
        elif action == "W":
            e -= value

    return abs(n) + abs(e)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
