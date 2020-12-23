import collections
import functools
import pathlib
from typing import List, NamedTuple

MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


class Edges(NamedTuple):
    top: str
    right: str
    bottom: str
    left: str


class Tile:
    tile_id: int
    rows: List[str]

    def __init__(self, tile_id, rows):
        self.tile_id = tile_id
        self.rows = rows

    @functools.cached_property
    def edges(self):
        return Edges(
            top=self.rows[0],
            right="".join(row[-1] for row in self.rows),
            bottom=self.rows[-1],
            left="".join(row[0] for row in self.rows),
        )

    top = property(lambda self: self.edges.top)
    right = property(lambda self: self.edges.right)
    bottom = property(lambda self: self.edges.bottom)
    left = property(lambda self: self.edges.left)

    @functools.lru_cache()
    def orientations(self):
        return [
            (self.flip() if flip else self).rotate90(rot)
            for rot in range(4)
            for flip in (False, True)
        ]

    @classmethod
    def from_input(cls, input_data):
        input_data = input_data.splitlines()
        _, _, tile_id = input_data.pop(0).partition(" ")
        tile_id = int(tile_id.rstrip(":"))

        return cls(tile_id=tile_id, rows=input_data)

    def flip(self):
        return type(self)(tile_id=self.tile_id, rows=[row[::-1] for row in self.rows])

    def rotate90(self, times=1):
        rows = self.rows.copy()

        for _ in range(times % 4):
            rows = ["".join(fs) for fs in zip(*reversed(rows))]

        return type(self)(tile_id=self.tile_id, rows=rows)

    def edgeless(self):
        return type(self)(tile_id=self.tile_id, rows=[row[1:-1] for row in self.rows[1:-1]])

    def __str__(self):
        return "\n".join(self.rows)

    def __repr__(self):
        return f"<{type(self).__name__} {repr(self.tile_id)}>"

    def __eq__(self, other):
        return isinstance(other, Tile) and self.tile_id == other.tile_id and self.rows == other.rows

    def __hash__(self):
        return hash((self.tile_id, *self.rows))


def compute(data):
    """
    >>> compute(pathlib.Path(__file__).with_name("sample.txt").read_text())
    273
    """
    tiles = {(tile := Tile.from_input(inp)).tile_id: tile for inp in data.split("\n\n")}

    edge_tiles = collections.defaultdict(lambda: collections.defaultdict(dict))

    for tile in tiles.values():
        for oriented_tile in tile.orientations():
            for edge_pos, edge in oriented_tile.edges._asdict().items():
                edge_tiles[edge][oriented_tile.tile_id][edge_pos] = oriented_tile

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
                assert False, f"illegal number of common edges: {common}"

            s[tile].add(edge)

    def pop_tile(tile_set, top=None, right=None, bottom=None, left=None):
        candidates = None

        for pos, constr in dict(top=top, right=right, bottom=bottom, left=left).items():
            constr_candidates = set()
            if constr is None:
                continue
            else:
                for tile_id, pos_map in edge_tiles[constr].items():
                    if tile_id not in tile_set:
                        continue
                    if pos in pos_map:
                        constr_candidates.add(pos_map[pos])

            if candidates is None:
                candidates = constr_candidates
            else:
                candidates &= constr_candidates

        tile = next(iter(candidates))
        del tile_set[tile.tile_id]
        return tile

    square_width = int(len(tiles) ** 0.5)

    def first_row():
        row = [
            curr_tile := next(
                tile
                for tile_id, common_edges in corner_tile_edges.items()
                for tile in tiles[tile_id].orientations()
                if tile.left not in common_edges
                if tile.top not in common_edges
            )
        ]
        del corner_tile_edges[curr_tile.tile_id]

        return (
            row
            + [
                curr_tile := pop_tile(border_tile_edges, left=curr_tile.right)
                for _ in range(square_width - 2)
            ]
            + [pop_tile(corner_tile_edges, left=curr_tile.right)]
        )

    def mid_row(row_before):
        return (
            [curr_tile := pop_tile(border_tile_edges, top=row_before[0].bottom)]
            + [
                curr_tile := pop_tile(
                    inside_tile_edges, top=row_before[i].bottom, left=curr_tile.right
                )
                for i in range(1, square_width - 1)
            ]
            + [pop_tile(border_tile_edges, top=row_before[-1].bottom, left=curr_tile.right)]
        )

    def last_row(row_before):
        return (
            [curr_tile := pop_tile(corner_tile_edges, top=row_before[0].bottom)]
            + [
                curr_tile := pop_tile(
                    border_tile_edges, top=row_before[i].bottom, left=curr_tile.right
                )
                for i in range(1, square_width - 1)
            ]
            + [pop_tile(corner_tile_edges, top=row_before[-1].bottom, left=curr_tile.right)]
        )

    rows = (
        [curr_row := first_row()]
        + [curr_row := mid_row(curr_row) for _ in range(square_width - 2)]
        + [last_row(curr_row)]
    )

    image = [
        "".join(sym_row)
        for row in rows
        for sym_row in zip(*(str(tile.edgeless()).splitlines() for tile in row))
    ]

    image_width = len(image)

    for monster in Tile(666, rows=MONSTER).orientations():
        monster_height = len(monster.rows)
        monster_width = len(monster.rows[0])

        count = sum(
            all(
                monster_sym == image_sym or monster_sym == " "
                for monster_row, image_row in zip(
                    monster.rows, image[y_idx : y_idx + monster_height]
                )
                for monster_sym, image_sym in zip(
                    monster_row, image_row[x_idx : x_idx + monster_width]
                )
            )
            for x_idx in range(image_width - monster_width)
            for y_idx in range(image_width - monster_height)
        )

        if count:
            break
    else:
        assert False, "no monsters found"

    image_hash_count = sum(image_row.count("#") for image_row in image)
    monster_hash_count = sum(monster_row.count("#") for monster_row in MONSTER)

    return image_hash_count - count * monster_hash_count


def main():
    input_path = pathlib.Path(__file__).with_name("input.txt")
    # input_path = pathlib.Path(__file__).with_name("sample.txt")

    print(compute(input_path.read_text()))


if __name__ == "__main__":
    main()
