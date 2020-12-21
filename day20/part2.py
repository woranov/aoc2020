import collections
import pathlib
from pprint import pprint
from typing import NamedTuple


class Edges(NamedTuple):
    top: str
    right: str
    bottom: str
    left: str


class Tile(NamedTuple):
    tile_id: int
    edges: Edges

    @classmethod
    def from_input(cls, input_data):
        input_data = input_data.splitlines()
        _, _, tile_id = input_data.pop(0).partition(" ")
        tile_id = int(tile_id.rstrip(":"))

        """
        a b c
        d   e
        f g h
        """
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

    def __repr__(self):
        return f"<{type(self).__name__} {repr(self.tile_id)}>"


"""
SAMPLE

1951    2311    3079
2729    1427    2473
2971    1489    1171
"""


def compute(data):
    """
    >>> compute(pathlib.Path(__file__).with_name("sample.txt").read_text())
    20899048083289
    """
    tiles = {(tile := Tile.from_input(inp)).tile_id: tile for inp in data.split("\n\n")}

    permutations = {
        (tile.tile_id, r, bool(f)): (tile.flip() if f else tile).rotate90(r)
        for tile in tiles.values()
        for r in range(4)
        for f in range(2)
    }

    edge_tiles = collections.defaultdict(lambda: collections.defaultdict(list))

    for (tid, r, f), permutation in permutations.items():
        for edge_pos, edge in permutation.edges._asdict().items():
            edge_tiles[edge][tid].append((r, f, edge_pos))

    tiles_by_common_edges = collections.Counter(
        tile for tiles in edge_tiles.values() for tile in tiles if len(tiles) == 2
    )

    corner_tile_edges = collections.defaultdict(set)
    border_tile_edges = collections.defaultdict(set)
    inside_tile_edges = collections.defaultdict(set)

    for edge, edge_ts in edge_tiles.items():
        if len(edge_ts) != 2:
            continue
        for tile in edge_ts:
            common = tiles_by_common_edges[tile]
            if common == 4:
                s = corner_tile_edges
            elif common == 6:
                s = border_tile_edges
            elif common == 8:
                s = inside_tile_edges
            else:
                assert False

            s[tile].add(edge)

    print("corner", end="  ")
    pprint(corner_tile_edges)
    print("border", end="  ")
    pprint(border_tile_edges)
    print("inside", end="  ")
    pprint(inside_tile_edges)


def main():
    # input_path = pathlib.Path(__file__).with_name("input.txt")
    input_path = pathlib.Path(__file__).with_name("sample.txt")

    print(compute(input_path.read_text()))


if __name__ == "__main__":
    main()
