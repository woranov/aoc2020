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
    10
    """
    tiles_facing_black = set()

    for steps in data:
        position = sum(DIRECTIONS_DELTAS[direction] for direction in DIRECTIONS_PAT.findall(steps))
        tiles_facing_black ^= {position}

    return len(tiles_facing_black)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
