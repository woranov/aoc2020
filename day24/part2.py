import collections
import re

_TESTCASE = """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""".strip().splitlines()


DIRECTIONS_PAT = re.compile("e|se|sw|w|nw|ne")
DIRECTIONS_DELTAS = {
    "e": 1 + 0j,
    "se": 0.5 - 0.5j,
    "sw": -0.5 - 0.5j,
    "w": -1 + 0j,
    "nw": -0.5 + 0.5j,
    "ne": 0.5 + 0.5j,
}


def compute(data):
    """
    >>> compute(_TESTCASE)
    2208
    """
    tiles_facing_black = collections.defaultdict(bool)

    for steps in data:
        position = sum(DIRECTIONS_DELTAS[direction] for direction in DIRECTIONS_PAT.findall(steps))
        tiles_facing_black[position] ^= True

    for _ in range(100):
        neighbor_counter = collections.Counter()

        for tile, facing_black in tiles_facing_black.items():
            if facing_black:
                # always include this tile but dont change the count if it was already included
                neighbor_counter[tile] += 0
                for delta in DIRECTIONS_DELTAS.values():
                    neighbor = tile + delta
                    neighbor_counter[neighbor] += 1

        for tile, black_nbs in tuple(neighbor_counter.items()):
            should_flip = black_nbs not in (1, 2) if tiles_facing_black[tile] else black_nbs == 2
            if not should_flip:
                del neighbor_counter[tile]

        for tile in neighbor_counter:
            tiles_facing_black[tile] ^= True

    return sum(tiles_facing_black.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
