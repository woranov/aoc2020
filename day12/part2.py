from typing import NamedTuple


class Vec2(NamedTuple):
    x: int
    y: int

    def rotate90(self, times):
        times %= 4
        x, y = self.x, self.y

        for _ in range(times):
            x, y = y, -x

        return self._replace(x=x, y=y)

    def rotate(self, degrees):
        if not degrees % 90 == 0.0:
            raise NotImplementedError
        else:
            return self.rotate90(degrees // 90)

    def __neg__(self):
        return self._replace(x=-self.x, y=-self.y)

    def __add__(self, other):
        if isinstance(other, Vec2):
            return self._replace(x=self.x + other.x, y=self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return self._replace(x=self.x * other.x, y=self.y * other.y)
        elif isinstance(other, int):
            return self._replace(x=self.x * other, y=self.y * other)
        else:
            return NotImplemented

    def __abs__(self):
        return abs(self.x) + abs(self.y)


DIRECTIONS = {
    "N": Vec2(0, 1),
    "E": Vec2(1, 0),
    "S": Vec2(0, -1),
    "W": Vec2(-1, 0),
}


def compute(data):
    """
    >>> compute(["F10", "N3", "F7", "R90", "F11"])
    286
    """
    ship = Vec2(0, 0)
    waypoint = Vec2(10, 1)

    for instruction in data:
        action = instruction[0]
        value = int(instruction[1:])

        if action in DIRECTIONS:
            waypoint += DIRECTIONS[action] * value
        elif action == "L":
            waypoint = waypoint.rotate(-value)
        elif action == "R":
            waypoint = waypoint.rotate(value)
        elif action == "F":
            ship += waypoint * value

    return abs(ship)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
