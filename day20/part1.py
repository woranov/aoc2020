import collections
import pathlib
from typing import NamedTuple


class Edges(NamedTuple):
    top: str
    right: str
    bottom: str
    left: str


# noinspection PyArgumentList
class Tile(NamedTuple):
    tile_id: int
    edges: Edges

    @classmethod
    def from_input(cls, input_data):
        input_data = input_data.splitlines()
        _, _, tile_id = input_data.pop(0).partition(" ")
        tile_id = int(tile_id.rstrip(":"))

        edges = Edges(
            top=input_data[0],
            right="".join(row[-1] for row in input_data),
            bottom=input_data[-1],
            left="".join(row[0] for row in input_data),
        )

        return cls(tile_id=tile_id, edges=edges)

    def flip(self):
        new_top = self.edges.top[::-1]
        new_bottom = self.edges.bottom[::-1]
        new_left = self.edges.right
        new_right = self.edges.left

        return self._replace(edges=Edges(new_top, new_right, new_bottom, new_left))

    def rotate90(self, times=1):
        new_top, new_right, new_bottom, new_left = self.edges
        for _ in range(times):
            (new_top, new_right, new_bottom, new_left) = (
                new_left[::-1],
                new_top,
                new_right[::-1],
                new_bottom,
            )

        return self._replace(edges=Edges(new_top, new_right, new_bottom, new_left))

    def __str__(self):
        rows = []

        rows.append(self.edges.top)

        fill = "." * (len(self.edges.top) - 2)

        for left, right in zip(self.edges.left[1:-1], self.edges.right[1:-1]):
            rows.append(f"{left}{fill}{right}")

        rows.append(self.edges.bottom)

        return "\n".join(row.replace("", " ").strip() for row in rows)


def compute(data):
    """
    >>> compute(pathlib.Path(__file__).with_name("sample.txt").read_text())
    20899048083289
    """
    tiles = [Tile.from_input(inp) for inp in data.split("\n\n")]

    # some unnecessary data structures with unneeded extra information but it helps
    # with exploration, # and hopefully part 2

    permutations = {
        (tile.tile_id, r, f): (tile.flip() if f else tile).rotate90(r)
        for tile in tiles
        for r in range(2)
        for f in range(2)
    }

    edge_tiles = collections.defaultdict(lambda: collections.defaultdict(list))

    for (tid, r, f), permutation in permutations.items():
        for edge_pos, edge in permutation.edges._asdict().items():
            edge_tiles[edge][tid].append((r, f, edge_pos))

    tiles_by_unique_edges = collections.Counter(
        tile for tiles in edge_tiles.values() for tile in tiles if len(tiles) == 1
    )

    product = 1
    for tid, _ in tiles_by_unique_edges.most_common(4):
        product *= tid

    return product


def main():
    input_path = pathlib.Path(__file__).with_name("input.txt")
    # input_path = pathlib.Path(__file__).with_name("sample.txt")

    print(compute(input_path.read_text()))


if __name__ == "__main__":
    main()
